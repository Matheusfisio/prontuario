import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prontuario_offline.settings')
django.setup()

from agendamentos.views import geren_agenda
print("Função carregada com sucesso:", geren_agenda)
