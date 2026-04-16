from django.urls import path

from . import views


urlpatterns = [
    path('', views.registrar_asistencia, name='asistencia_formulario'),
    path('confirmacion/', views.confirmacion_asistencia, name='asistencia_confirmacion'),
]
