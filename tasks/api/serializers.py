from rest_framework import serializers

from tasks.models import Task
from users.models import User


class TaskAssignSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, allow_null=True)

    class Meta:
        model = Task
        fields = (
            'users',
        )


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
