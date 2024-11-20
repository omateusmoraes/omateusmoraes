from django import forms
from .models import Contasareceber  # Importando o modelo de contas a receber

class ContasareceberForm(forms.ModelForm):
    class Meta:
        model = Contasareceber
        fields = ['cliente', 'descricao', 'vencimento', 'valor']  # Alterado para cliente
