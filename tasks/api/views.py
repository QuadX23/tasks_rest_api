from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter

from tasks.api import serializers
from tasks.models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = serializers.TaskSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'name',
    )


class TaskAssignCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TaskAssignSerializer
    queryset = Task.objects.all()
