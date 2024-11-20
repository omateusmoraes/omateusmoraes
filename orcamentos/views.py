from django.shortcuts import render, redirect, get_object_or_404
from .models import Orcamento
from .forms import OrcamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def orcamento_list(request):
    orcamentos = Orcamento.objects.all()  # Busca todos os orçamentos
    return render(request, 'orcamentos.html', {'orcamentos': orcamentos})  # Use 'orcamentos' no plural
@login_required
def add_orcamento(request):
    if request.method == 'POST':
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orcamento_list')  # Redireciona para a lista após salvar
    else:
        form = OrcamentoForm()
    return render(request, 'orcamentos.html', {'form': form})  # Aqui pode ser apenas para adicionar
@login_required
def edit_orcamento(request, pk):
    orcamento = get_object_or_404(Orcamento, pk=pk)
    if request.method == 'POST':
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            form.save()
            return redirect('orcamento_list')
    else:
        form = OrcamentoForm(instance=orcamento)
    return render(request, 'orcamentos.html', {'form': form})
@login_required
def delete_orcamento(request, id):
    orcamento = get_object_or_404(Orcamento, pk=id)
    orcamento.delete()
    return redirect('orcamento_list')
