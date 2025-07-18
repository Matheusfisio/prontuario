from django.urls import path
from . import views

app_name = 'evolucoes'


urlpatterns = [
    path('<int:paciente_id>/evolucoes/', views.lista_evolucoes, name='lista_evolucoes'),
    path('<int:paciente_id>/evolucoes/nova/', views.nova_evolucao, name='nova_evolucao'),
    path('<int:paciente_id>/editar/<int:evolucao_id>/', views.editar_evolucao, name='editar_evolucao'),
    path('', views.listar_pacientes_para_evolucao, name='listar_pacientes'),
    path('', views.lista_pacientes_com_evolucao, name='lista_pacientes_com_evolucao'),
    path('<int:paciente_id>/nova/', views.nova_evolucao, name='nova_evolucao'),
    path('<int:paciente_id>/evolucoes/', views.lista_evolucoes_paciente, name='lista_evolucoes'),
    path('<int:paciente_id>/evolucoes/', views.lista_evolucoes, name='lista_evolucoes'),
    path('<int:evolucao_id>/editar/', views.editar_evolucao, name='editar_evolucao'),


]
