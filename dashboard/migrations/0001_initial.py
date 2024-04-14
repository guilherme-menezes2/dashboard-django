# Generated by Django 5.0.3 on 2024-04-08 01:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=1000)),
                ('data_tarefa', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
