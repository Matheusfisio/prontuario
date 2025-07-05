from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('', views.lista_pacientes, name='lista_pacientes'),
    path('novo/', views.cadastrar_paciente, name='cadastrar_paciente'),
    path('<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('<int:pk>/excluir/', views.excluir_paciente, name='excluir_paciente'),
    path('<int:paciente_id>/detalhes/', views.detalhes_paciente, name='detalhes_paciente'),


]
