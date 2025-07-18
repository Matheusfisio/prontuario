from django.contrib import admin
from .models import Agendamento
from datetime import datetime, date

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data', 'hora_inicio', 'mostrar_duracao', 'fisioterapeuta')
    search_fields = ('paciente__nome', 'fisioterapeuta__username')
    list_filter = ('data', 'fisioterapeuta')

    def mostrar_duracao(self, obj):
        if obj.hora_fim and obj.hora_inicio:
            duracao = datetime.combine(date.min, obj.hora_fim) - datetime.combine(date.min, obj.hora_inicio)
            return str(duracao)
        return "-"
    mostrar_duracao.short_description = 'Duração'