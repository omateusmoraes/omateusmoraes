from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def menu(request):
    return render(request, 'menu.html')
@login_required
def clientes(request):
    return render(request, 'clientes.html')
@login_required
def estoque(request):
    return render(request, 'estoque.html')
@login_required
def faturamento(request):
    return render(request, 'faturamento.html')
@login_required
def agendamentos(request):
    return render(request, 'agendamentos.html')
@login_required
def contasapagar(request):
    return render(request, 'contasapagar.html')
@login_required
def contasareceber(request):
    return render(request, 'contasareceber.html')
@login_required

def orcamentos(request):
    return render(request, 'orcamentos.html')

@login_required
def menu_view(request):
    return render(request, 'menu.html')

