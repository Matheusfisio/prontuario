
from django.urls import path
from . import views

app_name = 'avaliacoes'

urlpatterns = [
    
    path('', views.avaliacoes_inicio, name='avaliacoes_inicio'),
    path('<int:paciente_id>/nova/', views.nova_avaliacao, name='nova_avaliacao'),
    path('<int:paciente_id>/listar/', views.listar_avaliacoes, name='listar_avaliacoes'),
    path('editar/<uuid:avaliacao_id>/', views.editar_avaliacao, name='editar_avaliacao'),
    path('excluir/<uuid:avaliacao_id>/', views.excluir_avaliacao, name='excluir_avaliacao'),
]
