from django.db import models

class Fatura(models.Model):
    data = models.DateField()
    cliente = models.CharField(max_length=100)
    descricao_servico = models.TextField()
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)
    valor_material = models.DecimalField(max_digits=10, decimal_places=2)

    def valor_total(self):
        return self.valor_servico + self.valor_material
