from rest_framework import viewsets
from .models import Tarefas
from .serializers import TarefasSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied


class TarefasViewSet(viewsets.ModelViewSet):
    queryset = Tarefas.objects.all()
    serializer_class = TarefasSerializer 
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tarefas.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        tarefa = self.get_object()
        if tarefa.owner != request.user:
            raise PermissionDenied("Você não tem permissão para modificar esta tarefa.")
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        tarefa = self.get_object()
        if tarefa.owner != request.user:
            raise PermissionDenied("Você não tem permissão para excluir esta tarefa.")
        return super().destroy(request, *args, **kwargs)