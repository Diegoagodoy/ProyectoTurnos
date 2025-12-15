from django.urls import path
from . import views

app_name = 'turnos'

urlpatterns = [
    path('', views.lista_turnos, name='lista_turnos'),
    path('medicos/', views.gestionar_medicos, name='gestionar_medicos'),
    path('especialidades/', views.gestionar_especialidades,name='gestionar_especialidades'),
    path('pacientes/', views.gestionar_pacientes, name='gestionar_pacientes'),
]

