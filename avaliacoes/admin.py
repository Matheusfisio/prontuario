
from django.contrib import admin
from .models import Avaliacao

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['paciente', 'fisioterapeuta', 'data']
    list_filter = ['data', 'fisioterapeuta']
