import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    # created_at = django_filters.DateFromToRangeFilter()
    due_date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Task
        fields = ['completed', 'priority', 'due_date']