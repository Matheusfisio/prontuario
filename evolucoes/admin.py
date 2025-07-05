
from django.contrib import admin
from .models import Evolucao



@admin.register(Evolucao)
class EvolucaoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data')
    list_filter = ('data',)
    search_fields = ('paciente__nome', 'texto')