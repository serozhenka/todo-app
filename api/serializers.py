from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email')


class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user', 'is_completed')

    def get_created(self, obj):
        return obj.created.strftime('%d %B %H:%M')


class TaskSerializerAllowUpdate(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    created = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user', )

    def get_created(self, obj):
        return obj.created.strftime('%d %B %H:%M')



