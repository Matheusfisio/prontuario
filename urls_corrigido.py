from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('formularios/', include('formularios.urls')),
    path('avaliacoes/', include('avaliacoes.urls')),
    path('evolucoes/', include('evolucoes.urls')),
    # path('pacientes/', include('pacientes.urls')),  # Ativar quando tiver views
    path('', auth_views.LoginView.as_view(template_name='registration/login.html')),
]
