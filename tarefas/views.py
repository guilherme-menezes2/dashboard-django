from django.shortcuts import render, redirect
from django.contrib import messages
from tarefas.models import Tarefa
from tarefas.forms import TarefaForms

def tarefas(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a dashboard')
        return redirect('login')

    tarefas = Tarefa.objects.all().order_by('data_tarefa').filter(completa=False)

    return render(request, 'tarefas/tarefas.html', {'cards': tarefas})
        
def deletar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.get(id=tarefa_id)
    tarefa.delete()
    messages.error(request, 'Tarefa deletada com sucesso')
    return redirect('tarefas')

def nova_tarefa(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Faça login para acessar a dashboard')
        return redirect('login')
    
    form = TarefaForms
    if request.method == 'POST':
        form = TarefaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas')
    
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

def filtro_tarefa(request):
    tarefas = Tarefa.objects.order_by('data_tarefa').filter(completa=False)
    if 'start_date' in request.GET:
        data_a_buscar = request.GET['start_date']
        if data_a_buscar:
            tarefas = tarefas.filter(data_tarefa__date=data_a_buscar)
        return render(request, 'tarefas/tarefas.html', {'cards': tarefas})
    
def finalizar_tarefa(request, tarefa_id):
    tarefa = Tarefa.objects.filter(id=tarefa_id)
    tarefa.update(completa=True)
    messages.error(request, 'Tarefa Finalizada com sucesso')
    return redirect('tarefas')
