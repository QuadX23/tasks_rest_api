from rest_framework import generics, viewsets
from rest_framework.filters import SearchFilter

from users.api import serializers
from users.models import User, TaskReview


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        'position',
    )


class TaskReviewCreateAPIView(generics.CreateAPIView):
    serializer_class = serializers.TaskReviewSerializer
    queryset = TaskReview.objects.all()

    def get_serializer_context(self):
        performer_id = self.request.query_params.get('performer_id')
        return {
            'user_id': self.kwargs['pk'],
            'performer_id': performer_id
        }


class TasksOnReviewListAPIView(generics.ListAPIView):
    serializer_class = serializers.TaskOnReviewSerializer

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return TaskReview.objects.select_related('user', 'task', 'task_performer').filter(user=user_id)


class ReviewersListAPIView(generics.ListAPIView):
    serializer_class = serializers.ReviewersSerializer
    queryset = User.objects.prefetch_related('tasks_on_review').filter(reviewer__isnull=False).distinct()
