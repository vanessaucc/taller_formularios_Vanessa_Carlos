from django.urls import path

from . import views


urlpatterns = [
    path('', views.registrar_solicitud, name='solicitudes_formulario'),
    path('confirmacion/', views.confirmacion_solicitud, name='solicitudes_confirmacion'),
]
