from rest_framework import viewsets
from .models import Tarefas
from .serializers import TarefasSerializer
from rest_framework.permissions import IsAuthenticated


class TarefasViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer 
    permission_classes = [IsAuthenticated]
