# models.py
from django.db import models

class Contasapagar(models.Model):
    fornecedor = models.CharField(max_length=100)
    descricao = models.CharField(max_length=200)
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.fornecedor} - {self.descricao}"


