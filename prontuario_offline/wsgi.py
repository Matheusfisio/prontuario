import os
from django.core.wsgi import get_wsgi_application

# Aponta para o settings.py do seu projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prontuario_offline.settings')

# Cria a aplicação WSGI que o Django precisa para iniciar o servidor
application = get_wsgi_application()
