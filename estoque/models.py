from django.db import models


class Item(models.Model):
    item = models.CharField(max_length=100)
    quantidade = models.IntegerField()
    unidade = models.CharField(max_length=50)
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.item
