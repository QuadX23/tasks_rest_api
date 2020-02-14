from django.urls import path

from . import views as api_views
from .views import UserViewSet, TaskReviewCreateAPIView, TasksOnReviewListAPIView, ReviewersListAPIView

users_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
users_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', users_list),
    path('<int:pk>/', users_detail),
    path('<int:pk>/review-task', TaskReviewCreateAPIView.as_view()),
    path('<int:pk>/tasks-on-review', TasksOnReviewListAPIView.as_view()),
    path('reviewers', ReviewersListAPIView.as_view()),
]
