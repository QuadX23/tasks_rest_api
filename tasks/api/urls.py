from django.urls import path

from . import views as api_views
from .views import TaskViewSet, TaskAssignCreateAPIView

tasks_list = TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
tasks_detail = TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('', tasks_list),
    path('<int:pk>/', tasks_detail),
    path('<int:pk>/assign/', TaskAssignCreateAPIView.as_view()),
]
