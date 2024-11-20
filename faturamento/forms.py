from django import forms
from .models import Fatura

class FaturaForm(forms.ModelForm):
    class Meta:
        model = Fatura
        fields = ['data', 'cliente', 'descricao_servico', 'valor_servico', 'valor_material']
