
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formularios/', include('formularios.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('evolucoes/', include('evolucoes.urls')),
    # Adicione outras rotas conforme necessário
]
