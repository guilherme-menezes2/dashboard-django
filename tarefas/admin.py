from django.contrib import admin
from tarefas.models import Tarefa

class ListandoTarefas(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'data_tarefa')

admin.site.register(Tarefa, ListandoTarefas)