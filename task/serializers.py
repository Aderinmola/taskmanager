from rest_framework import serializers
from .models import Task
from users.serializers import ProfileSerializer


class TaskSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'priority', 'created_at', 'due_date', 'owner']
        read_only_fields = ['created_at', 'due_date', 'owner']


class TaskCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'completed', 'priority', 'created_at', 'due_date', 'owner']
        read_only_fields = ['created_at', 'due_date', 'owner']


class TaskCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['completed']
        extra_kwargs = {
            'completed': {'required': True}
        }
