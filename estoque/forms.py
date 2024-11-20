from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item', 'quantidade', 'unidade', 'valor_unitario', 'valor_total']
