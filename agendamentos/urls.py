from django.urls import path
from . import views
from agendamentos.views import geren_agenda
from agendamentos.views import pagina_agenda 
from .views import geren_agenda

app_name = 'agendamentos'

urlpatterns = [
    path('lista', views.lista_agendamentos, name='lista_agendamentos'),
    path('novo/', views.novo_agendamento, name='novo_agendamento'),
    path('<int:agendamento_id>/editar/', views.editar_agendamento, name='editar_agendamento'),
    path('<int:agendamento_id>/excluir/', views.excluir_agendamento, name='excluir_agendamento'),
    path('buscar/<str:data_str>/', views.buscar_agendamentos_por_data, name='buscar_agendamentos'),
    path('horarios/', views.horarios_por_data, name='horarios_por_data'),
    path('eventos/', views.eventos_json, name='eventos_json'),
    path('horarios_json/', views.horarios_json, name='horarios_json'),
    path('', views.geren_agenda, name='agenda_inicio'),
   


]
