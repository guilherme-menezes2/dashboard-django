from django.urls import path
from tarefas.views import tarefas, deletar_tarefa, nova_tarefa, filtro_tarefa, finalizar_tarefa

urlpatterns = [
    path('tarefas', tarefas, name='tarefas'),
    path('deletar_tarefa/<int:tarefa_id>', deletar_tarefa, name='deletar_tarefa'),
    path('nova_tarefa', nova_tarefa, name='nova_tarefa'),
    path('filtro_tarefa', filtro_tarefa, name='filtro_tarefa'),
    path('finalizar_tarefa/<int:tarefa_id>', finalizar_tarefa, name='finalizar_tarefa'),
]