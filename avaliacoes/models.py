from django.db import models
from django.contrib.auth.models import User
from pacientes.models import Paciente

class Avaliacao(models.Model):
    AREA_CHOICES = [
        ("Membro Superior", "Membro Superior"),
        ("Membro Inferior", "Membro Inferior"),
        ("Coluna Cervical", "Coluna Cervical"),
        ("Coluna Torácica", "Coluna Torácica"),
        ("Coluna Lombar", "Coluna Lombar"),
    ]

    ARTICULACAO_SUPERIOR = [
        ("Ombro", "Ombro"),
        ("Cotovelo", "Cotovelo"),
        ("Punho", "Punho"),
        ("Mão", "Mão"),
        ("Dedos", "Dedos"),
    ]

    ARTICULACAO_INFERIOR = [
        ("Quadril", "Quadril"),
        ("Joelho", "Joelho"),
        ("Tornozelo", "Tornozelo"),
        ("Pé", "Pé"),
        ("Dedos do pé", "Dedos do pé"),
    ]

    COLUNA_CERVICAL = [
        ("C1-C2", "C1-C2"),
        ("C3-C4", "C3-C4"),
        ("C5-C6", "C5-C6"),
        ("C7", "C7"),
    ]

    COLUNA_TORACICA = [
        ("T1-T4", "T1-T4"),
        ("T5-T8", "T5-T8"),
        ("T9-T12", "T9-T12"),
    ]

    COLUNA_LOMBAR = [
        ("L1-L2", "L1-L2"),
        ("L3-L4", "L3-L4"),
        ("L5-S1", "L5-S1"),
    ]

    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fisioterapeuta = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    area = models.CharField(max_length=30, choices=AREA_CHOICES)
    articulacao = models.CharField(max_length=30)
    medidas_json = models.JSONField()

    def __str__(self):
        return f"{self.paciente.nome} - {self.area} - {self.articulacao} ({self.data})"
