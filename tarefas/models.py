from django.db import models
from datetime import datetime

class Tarefa(models.Model):
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.CharField(max_length=1000, null=False, blank=False)
    data_tarefa = models.DateTimeField(default=datetime.now, blank=False)
    completa = models.BooleanField(default=False)