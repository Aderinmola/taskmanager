from rest_framework import viewsets, permissions
from .models import Board, Task
from .serializers import BoardSerializer, TaskSerializer
from rest_framework.exceptions import ValidationError


class BoardViewSet(viewsets.ModelViewSet):
    serializer_class = BoardSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Board.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # You can only update when owner equals currently login user


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(board__owner=self.request.user)

    def perform_create(self, serializer):
        board = serializer.validated_data.get('board')
        if board.owner != self.request.user:
            raise ValidationError("You do not have permission to add tasks to this board.")
        serializer.save()
