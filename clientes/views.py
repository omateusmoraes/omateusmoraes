# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
@login_required
def clientes_list(request):
    clients = Cliente.objects.all()
    return render(request, 'clientes.html', {'clients': clients})
@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})
@login_required
def edit_client(request, pk):
    client = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('clientes_list')
    else:
        form = ClienteForm(instance=client)
    return render(request, 'cliente_form.html', {'form': form})
@login_required
def delete_client(request, pk):
    client = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        client.delete()
        return redirect('clientes_list')
    return render(request, 'cliente_confirm_delete.html', {'client': client})


