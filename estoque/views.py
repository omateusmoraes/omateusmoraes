# Importações necessárias do Django
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm
from django.contrib.auth.decorators import login_required



@login_required # View para renderizar a página inicial do controle de estoque
def estoque_list(request):
    items = Item.objects.all()  # Obtém todos os itens do estoque do banco de dados
    return render(request, 'estoque.html', {'items': items})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('estoque_list')
        else:
            form = ItemForm()
        return render(request,'estoque_form.html')  # Redireciona de volta para a página de estoque após adicionar

@login_required # View para editar um item existente no estoque
def edit_item(request, pk):
    items = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
            form = ItemForm(request.POST, instance=items)
            if form.is_valid():
                form.save()
                return redirect('estoque_list')
            else:
                form = ItemForm(instance=items)
            return render(request, 'estoque_form.html', {'form':form}) # Redireciona de volta para a página de estoque após editar

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('estoque_list')
    else:
        # Criar um formulário vazio para passar para o template
        form = ItemForm(instance=item)
    return render(request, 'estoque_confirm_delete.html', {'item': item, 'form': form})
