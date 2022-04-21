from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)