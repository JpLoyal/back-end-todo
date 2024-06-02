from rest_framework import serializers
from .models import Tarefas


class TarefasSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Tarefas
        fields = ['id', 'descricao', 'data', 'horario', 'status', 'owner']