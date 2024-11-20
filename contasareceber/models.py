from django.db import models

class Contasareceber(models.Model):
    cliente = models.CharField(max_length=100)  # Alterado para cliente
    descricao = models.CharField(max_length=200)
    vencimento = models.DateField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cliente} - {self.descricao}"
