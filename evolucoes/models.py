
from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente
from django.utils import timezone

class Evolucao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='evolucoes')
    fisioterapeuta = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    editado = models.BooleanField(default=False)
    data_edicao = models.DateTimeField(null=True, blank=True)
    versao_original = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='versoes')

    def __str__(self):
        return f"{self.paciente.nome} - {self.data.strftime('%d/%m/%Y %H:%M')}"
    

    