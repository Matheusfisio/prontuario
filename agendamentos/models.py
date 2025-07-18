from django.db import models
from pacientes.models import Paciente
from django.contrib.auth.models import User

class Agendamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='agendamentos')
    fisioterapeuta = models.ForeignKey(User, on_delete=models.CASCADE, related_name='agendamentos')
    data = models.DateField()
    hora_inicio = models.TimeField()
    hora_fim = models.TimeField()
    tipo_atendimento = models.CharField(
        max_length=100,
        choices=[
            ('motor', 'Fisioterapia Motora'),
            ('respiratoria', 'Fisioterapia Respiratória'),
            ('neurologica', 'Fisioterapia Neurológica'),
            ('avaliacao', 'Avaliação'),
            ('Osteo', 'Osteopatia'),
        ],
        default='motor'
    )
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.paciente.nome_completo} - {self.data_hora.strftime("%d/%m/%Y %H:%M")}'

    class Meta:
        ordering = ['data', 'hora_inicio']
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'


