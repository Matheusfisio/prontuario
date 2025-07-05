
from django.db import models
from django.contrib.auth.models import User

class FormularioAvaliacao(models.Model):
    nome = models.CharField(max_length=255)
    profissional = models.ForeignKey(User, on_delete=models.CASCADE)
    estrutura_json = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.nome} ({self.profissional.username})"
