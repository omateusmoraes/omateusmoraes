# forms.py

from django import forms
from .models import Contasapagar

class ContasapagarForm(forms.ModelForm):
    class Meta:
        model = Contasapagar
        fields = ['fornecedor', 'descricao', 'vencimento', 'valor']
