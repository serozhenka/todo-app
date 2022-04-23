from rest_framework import viewsets
from .serializers import TaskSerializer, TaskSerializerAllowUpdate
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = 'pk'

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.order_by('-created')

    def get_serializer_class(self):
        if self.action in ['update', 'partial_update']:
            return TaskSerializerAllowUpdate
        return TaskSerializer