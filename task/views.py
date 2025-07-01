from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from .filters import TaskFilter

from .models import Task
from .serializers import (
    TaskSerializer,
    TaskCreateSerializer,
    TaskCompleteSerializer
)
from rest_framework.exceptions import ValidationError


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action == 'create' or 'put' or 'patch':
            return TaskCreateSerializer
        return TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @action(detail=True, methods=['patch'], url_path='task_completed')
    def task_completed(self, request, pk=None):
        try:
            task = self.get_object()

        except Task.DoesNotExist:
            return Response({'detail': 'Task not found.'}, status=status.HTTP_404_NOT_FOUND)


        if task.owner != request.user:
            return Response({'detail': 'Not authorized to modify this task.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = TaskCompleteSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Task marked as completed.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

