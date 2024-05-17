from rest_framework import viewsets
from .models import Tarefas
from .serializers import TarefasSerializer


class TarefasViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer 
