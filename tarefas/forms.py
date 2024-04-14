from django import forms
from tarefas.models import Tarefa

class TarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        exclude = ['completa',]
        labels = {'descricao':'Descrição', 'data_tarefa':'Data da Tarefa'}

        widgets = {
            'nome':forms.TextInput(),
            'descricao':forms.Textarea(),
            'data_tarefa':forms.DateTimeInput(format=('%d/%m/%Y %H:%M'), attrs={'type':'datetime-local'}),
        }