from django import forms

class AccidentPredictionForm(forms.Form):
    FECHA_DEL_ACCIDENTE = forms.DateField(
        label="Fecha del Accidente",
        required=True,
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    DIA_DE_LA_SEMANA = forms.ChoiceField(
        label="Día de la Semana",
        choices=[('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miércoles'), ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes')],
        required=True,
    )
    ENTIDAD_FEDERATIVA_DEL_VEHICULO = forms.ChoiceField(
        label="Entidad Federativa del Vehículo",
        choices=[('CDMX', 'CDMX'), ('VERACRUZ', 'Veracruz'), ('JALISCO', 'Jalisco')],
        required=True,
    )
    CONDICIONES_NATURALES = forms.ChoiceField(
        label="Condiciones Naturales",
        choices=[('DESPEJADO', 'Despejado'), ('LLUVIA', 'Lluvia'), ('NIEBLA', 'Niebla')],
        required=True,
    )
    ESTADO_DE_LA_VIA = forms.ChoiceField(
        label="Estado de la Vía",
        choices=[('BUENO', 'Bueno'), ('MALO', 'Malo')],
        required=True,
    )
    TANGENTE = forms.ChoiceField(
        label="Tangente",
        choices=[('RECTA', 'Recta'), ('CURVA', 'Curva')],
        required=True,
    )
    RESTRICCIONES_DE_LA_VIA = forms.ChoiceField(
        label="Restricciones de la Vía",
        choices=[('NINGUNA', 'Ninguna'), ('SEMAFORO', 'Semáforo')],
        required=True,
    )
    TIPO_DE_ACCIDENTE = forms.ChoiceField(
        label="Tipo de Accidente",
        choices=[('CHOQUE', 'Choque'), ('VOLCADURA', 'Volcadura')],
        required=True,
    )
    FORMA_DE_ACCIDENTARSE = forms.ChoiceField(
        label="Forma de Accidentarse",
        choices=[('ANGULO', 'Ángulo'), ('CHOQUE FRONTAL', 'Choque Frontal'), ('CHOQUE LATERAL', 'Choque Lateral'), ('ALCANCE', 'Alcance')],
        required=True,
    )
    CONTRA_QUE_FUE_EL_IMPACTO = forms.ChoiceField(
        label="Contra qué fue el Impacto",
        choices=[('VEHICULO', 'Vehículo'), ('MURO', 'Muro')],
        required=True,
    )
    CANTIDAD_DE_VEHICULOS = forms.IntegerField(
        label="Cantidad de Vehículos",
        required=True,
    )
    TIPO_DE_VEHICULO = forms.ChoiceField(
        label="Tipo de Vehículo",
        choices=[('AUTOMOVIL', 'Automóvil'), ('CAMIONETA', 'Camioneta'), ('MOTOCICLETA', 'Motocicleta'), ('OMNIBUS', 'Ómnibus')],
        required=True,
    )
    TIPO_DE_SERVICIO = forms.ChoiceField(
        label="Tipo de Servicio",
        choices=[('P-PARTICULAR', 'Particular'), ('P-COMERCIAL', 'Comercial'), ('OFICIAL', 'Oficial')],
        required=True,
    )
    SEXO_CONDUCTOR = forms.ChoiceField(
        label="Sexo del Conductor",
        choices=[('MASCULINO', 'Masculino'), ('FEMENINO', 'Femenino')],
        required=True,
    )
    CAUSA_ATRIBUIBLE_AL_CONDUCTOR = forms.ChoiceField(
        label="Causa Atribuible al Conductor",
        choices=[('IMPRUDENCIA', 'Imprudencia'), ('DESCONOCIDO', 'Desconocido')],
        required=True,
    )
