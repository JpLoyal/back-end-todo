# Generated by Django 5.0.6 on 2024-05-17 16:49

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=255)),
                ('data', models.DateField()),
                ('horario', models.TimeField()),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('concluida', 'Concluída')], default='pendente', max_length=20)),
            ],
        ),
    ]
