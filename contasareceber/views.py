from django.shortcuts import render, redirect, get_object_or_404
from .models import Contasareceber  # Modelo para contas a receber
from .forms import ContasareceberForm  # Formulário para contas a receber
from django.contrib.auth.decorators import login_required
@login_required
def contasareceber_list(request):
    contasareceber = Contasareceber.objects.all()
    return render(request, 'contasareceber.html', {'contasareceber': contasareceber})
@login_required
def add_contasareceber(request):
    if request.method == 'POST':
        form = ContasareceberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contasareceber_list')
    else:
        form = ContasareceberForm()
    return render(request, 'contasareceber.html', {'form': form})
@login_required
def edit_contasareceber(request, pk):
    contasareceber = get_object_or_404(Contasareceber, pk=pk)
    if request.method == 'POST':
        form = ContasareceberForm(request.POST, instance=contasareceber)
        if form.is_valid():
            form.save()
            return redirect('contasareceber_list')
    else:
        form = ContasareceberForm(instance=contasareceber)
    return render(request, 'contasareceber_form.html', {'form': form})
@login_required
def delete_contasareceber(request, pk):
    contasareceber = get_object_or_404(Contasareceber, pk=pk)
    if request.method == 'POST':
        contasareceber.delete()
        return redirect('contasareceber_list')
    return render(request, 'contasareceber_confirm_delete.html', {'contasareceber': contasareceber})
