from django.urls import path
from .views import CustomAuthToken, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('api/token/', CustomAuthToken.as_view(), name='api-token'),
    path('api/tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
]
