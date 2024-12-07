from django.urls import path
from .views import predict_accident_view

urlpatterns = [
    path('predict/', predict_accident_view, name='predict_accident_view'),
]