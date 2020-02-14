from rest_framework import serializers

from tasks.api.serializers import TaskSerializer
from tasks.models import Task
from users.models import User, TaskReview


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = (
            'is_superuser',
        )


class TasksFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        performer_id = self.context.get('performer_id', None)
        queryset = super().get_queryset()
        if not performer_id or not queryset:
            return None
        return queryset.filter(users=performer_id)


class TaskReviewSerializer(serializers.ModelSerializer):
    task = TasksFilteredPrimaryKeyRelatedField(queryset=Task.objects)

    class Meta:
        model = TaskReview
        fields = (
            'task',
        )

    def create(self, validated_data):
        user_id = self.context['user_id']
        task_performer_id = self.context['performer_id']
        validated_data['user'] = User.objects.get(pk=user_id)
        validated_data['task_performer'] = User.objects.get(pk=task_performer_id)
        return super().create(validated_data)


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'name',
            'position',
            'city'
        )


class TaskOnReviewSerializer(serializers.ModelSerializer):
    task = TaskSerializer()
    task_performer = TaskUserSerializer()

    class Meta:
        model = TaskReview
        exclude = ('id', 'user')


class ReviewersSerializer(serializers.ModelSerializer):
    tasks_on_review = TaskSerializer(many=True)

    class Meta:
        model = User
        exclude = (
            'tasks',
        )
