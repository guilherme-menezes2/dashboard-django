# Generated by Django 5.0.3 on 2024-04-14 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_tarefa_completa'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Tarefa',
        ),
    ]