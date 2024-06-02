from django.db import models
from django.conf import settings

import uuid

class Tarefas(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descricao = models.CharField(max_length=255)
    data = models.DateField()
    horario = models.TimeField()
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('concluida', 'Concluída'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name_plural = "Tarefas"

