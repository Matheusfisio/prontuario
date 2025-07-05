
from django.urls import path
from . import views

app_name = 'avaliacoes'

urlpatterns = [
    
    path('', views.avaliacoes_inicio, name='avaliacoes_inicio'),
    path('<int:paciente_id>/nova/', views.nova_avaliacao, name='nova_avaliacao'),
    path('<int:paciente_id>/listar/', views.listar_avaliacoes, name='listar_avaliacoes'),
]
