from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento
from .forms import AgendamentoForm
from django.contrib.auth.decorators import login_required

@login_required
def agendamento_list(request):
    appointments = Agendamento.objects.all()
    return render(request, 'agendamentos.html', {'appointments': appointments})
@login_required
def add_agendamento(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm()
    return render(request, 'agendamento_form.html', {'form': form})
@login_required
def edit_agendamento(request, agendamento_id):
    appointment = get_object_or_404(Agendamento, id=agendamento_id)
    if request.method == 'POST':
        form = AgendamentoForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('agendamento_list')
    else:
        form = AgendamentoForm(instance=appointment)
    return render(request, 'agendamento_form.html', {'form': form})
@login_required
def delete_agendamento(request, pk):
    agendamento = get_object_or_404(Agendamento, pk=pk)
    if request.method == 'POST':
        agendamento.delete()
        return redirect('agendamento_list')
    return render(request, 'agendamento_confirm_delete.html', {'agendamento': agendamento})


