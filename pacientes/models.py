# models.py em pacientes
from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    fisioterapeuta = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pacientes_fisioterapeuta')
    sexo = models.CharField(max_length=10, choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    observacoes = models.TextField(blank=True)
    diagnostico = models.TextField(blank=True)
    criado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pacientes_criados')

    def idade(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return self.nome


# models.py em evolucoes



# views.py em evolucoes

