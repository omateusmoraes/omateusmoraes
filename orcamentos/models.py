from django.db import models

class Orcamento(models.Model):
    cliente = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    endereco = models.TextField()
    descricao = models.TextField()
    materiais = models.TextField(blank=True, null=True)
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    pagamento = models.TextField(blank=True, null=True)
    prazo = models.CharField(max_length=100, blank=True, null=True)
    validade = models.DateField()

    def __str__(self):
        return self.cliente
