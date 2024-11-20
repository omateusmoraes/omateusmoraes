from django.db import models

class Agendamento(models.Model):
    cliente = models.CharField(max_length=100)
    servico = models.CharField(max_length=100)
    data = models.DateField()
    horario = models.TimeField()

    def __str__(self):
        return f"{self.cliente} - {self.servico} em {self.data} às {self.horario}"
