import pickle
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .forms import AccidentPredictionForm

from django.shortcuts import render


# Carga el modelo al iniciar
model_path = os.path.join(os.path.dirname(__file__), 'model', 'modelo_xgboost.pkl')


with open(model_path, 'rb') as file:
    model = pickle.load(file)


# Mapeos de categorías a valores numéricos
mappings = {
    'DIA DE LA SEMANA': {'LUNES': 0, 'MARTES': 1, 'MIERCOLES': 2, 'JUEVES': 3, 'VIERNES': 4},
    'CONDICIONES NATURALES': {'DESPEJADO': 0, 'LLUVIA': 1, 'NIEBLA': 2},
    'ESTADO DE LA VIA': {'BUENO': 0, 'MALO': 1},
    'TANGENTE': {'RECTA': 0, 'CURVA': 1},
    'RESTRICCIONES DE LA VIA': {'NINGUNA': 0, 'SEMAFORO': 1},
    'TIPO DE ACCIDENTE': {'CHOQUE': 0, 'VOLCADURA': 1},
    'FORMA DE ACCIDENTARSE': {'ANGULO': 0, 'CHOQUE FRONTAL': 1, 'CHOQUE LATERAL': 2, 'ALCANCE': 3},
    'CONTRA QUE FUE EL IMPACTO': {'VEHICULO': 0, 'MURO': 1},
    'TIPO DE VEHICULO': {'AUTOMOVIL': 0, 'CAMIONETA': 1, 'MOTOCICLETA': 2, 'OMNIBUS': 3},
    'TIPO DE SERVICIO PARA EL QUE SE OCUPAN LOS VEHICULOS': {'P-PARTICULAR': 0, 'P-COMERCIAL': 1, 'OFICIAL': 2},
    'SEXO CONDUCTOR': {'MASCULINO': 0, 'FEMENINO': 1},
    'CAUSA ATRIBUIBLE AL CONDUCTOR': {'IMPRUDENCIA': 0, 'DESCONOCIDO': 1},
    'ENTIDAD FEDERATIVA DEL VEHICULO': {'CDMX': 0, 'VERACRUZ': 1, 'JALISCO': 2},
}





@csrf_exempt  # Permite solicitudes POST sin token CSRF (solo para pruebas locales)




# Función para realizar la predicción
def predict_accident_view(request):
    prediction_text = None
    error_message = None

    if request.method == 'POST':
        form = AccidentPredictionForm(request.POST)
        if form.is_valid():
            try:
                # Convertir valores categóricos a numéricos
                features = [
                    int(form.cleaned_data['FECHA_DEL_ACCIDENTE'].strftime('%Y%m%d')),  # Convertir fecha a formato numérico
                    mappings['DIA DE LA SEMANA'][form.cleaned_data['DIA_DE_LA_SEMANA']],
                    mappings['ENTIDAD FEDERATIVA DEL VEHICULO'][form.cleaned_data['ENTIDAD_FEDERATIVA_DEL_VEHICULO']],
                    mappings['CONDICIONES NATURALES'][form.cleaned_data['CONDICIONES_NATURALES']],
                    mappings['ESTADO DE LA VIA'][form.cleaned_data['ESTADO_DE_LA_VIA']],
                    mappings['TANGENTE'][form.cleaned_data['TANGENTE']],
                    mappings['RESTRICCIONES DE LA VIA'][form.cleaned_data['RESTRICCIONES_DE_LA_VIA']],
                    mappings['TIPO DE ACCIDENTE'][form.cleaned_data['TIPO_DE_ACCIDENTE']],
                    mappings['FORMA DE ACCIDENTARSE'][form.cleaned_data['FORMA_DE_ACCIDENTARSE']],
                    mappings['CONTRA QUE FUE EL IMPACTO'][form.cleaned_data['CONTRA_QUE_FUE_EL_IMPACTO']],
                    form.cleaned_data['CANTIDAD_DE_VEHICULOS'],
                    mappings['TIPO DE VEHICULO'][form.cleaned_data['TIPO_DE_VEHICULO']],
                    mappings['TIPO DE SERVICIO PARA EL QUE SE OCUPAN LOS VEHICULOS'][form.cleaned_data['TIPO_DE_SERVICIO']],
                    mappings['SEXO CONDUCTOR'][form.cleaned_data['SEXO_CONDUCTOR']],
                    mappings['CAUSA ATRIBUIBLE AL CONDUCTOR'][form.cleaned_data['CAUSA_ATRIBUIBLE_AL_CONDUCTOR']],
                ]
                
                # Realizar la predicción
                prediction = model.predict([features])[0]

                # Imprimir el valor de la predicción 
                print(f"Valor predicho por el modelo: {prediction}")

                # Convertir la predicción numérica a texto 
                prediction_text = map_resultado(prediction)
            except Exception as e:
                error_message = f"Error al procesar la predicción: {str(e)}"
    else:
        form = AccidentPredictionForm()

    return render(request, 'predice/predict_form.html', {
        'form': form,
        'prediction': prediction_text, 
        'error_message': error_message,
    })

# Mapeo para los resultados del modelo
def map_resultado(resultado):
    resultados = {
        16: 'VELOCIDAD INMODERADA',
    10: 'NO RESPETAR CEDA EL PASO',
    14: 'OTRO',
    5: 'CAMBIAR CARRIL SIN PRECAUCIÓN',
    9: 'NO GUARDAR DISTANCIA',
    12: 'NO RESPETAR SEMÁFORO',
    4: 'CAMBIAR CARRIL SIN PRECAUCION',
    17: 'VUELTA EN "U"',
    15: 'REBASAR INDEBIDAMENTE',
    13: 'NO RESPETAR SEÑAL DE ALTO',
    11: 'NO RESPETAR SEMAFORO',
    2: 'ALCOHOL / DROGAS',
    6: 'CIRCULAR EN SENTIDO CONTRARIO',
    3: 'ALCOHOL/DROGAS',
    0: 'ABRIR PUERTA SIN PRECAUCION',
    8: 'EXCESO DE DIMENSIONES',
    1: 'ABRIR PUERTA SIN PRECAUCIÓN',
    }
    return resultados.get(resultado, 'Desconocido')