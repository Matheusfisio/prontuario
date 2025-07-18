from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from prontuario_offline import views as core_views
from agendamentos.views import pagina_agenda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('pacientes/', include(('pacientes.urls', 'pacientes'), namespace='pacientes')),
    path('formularios/', include('formularios.urls')),
    path('avaliacoes/', include('avaliacoes.urls', namespace='avaliacoes')),
    path('evolucoes/', include('evolucoes.urls', namespace='evolucoes')),
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('home/', core_views.home, name='home'),
    path('agendamentos/', include('agendamentos.urls', namespace='agendamentos')),

    
]
