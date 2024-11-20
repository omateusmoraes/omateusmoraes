from django.shortcuts import render, redirect, get_object_or_404
from .models import Fatura
from .forms import FaturaForm
from django.contrib.auth.decorators import login_required


@login_required
def faturamento_list(request):
    faturas = Fatura.objects.all()
    return render(request, 'faturamento.html', {'faturas': faturas})
@login_required
def faturamento_add(request):
    if request.method == 'POST':
        form = FaturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faturamento_list')
    else:
        form = FaturaForm()
    return render(request, 'faturamento_form.html', {'form': form})
@login_required
def faturamento_edit(request, pk):
    fatura = get_object_or_404(Fatura, pk=pk)
    if request.method == 'POST':
        form = FaturaForm(request.POST, instance=fatura)
        if form.is_valid():
            form.save()
            return redirect('faturamento_list')
    else:
        form = FaturaForm(instance=fatura)
    return render(request, 'faturamento_form.html', {'form': form})
@login_required
def fatura_delete(request, pk):
    fatura = get_object_or_404(Fatura, pk=pk)
    if request.method == 'POST':
        fatura.delete()
        return redirect('faturamento_list')
    else:
        form = FaturaForm(instance=fatura)
    return render(request, 'faturamento_delete_confirm.html', {'fatura': fatura})
