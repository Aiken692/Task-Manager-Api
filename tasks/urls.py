from django.urls import path
from .views import RegisterUserView, TaskListView, TaskCreateView, UserListView, TaskUpdateView, TaskDeleteView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('users/', UserListView.as_view(), name='user_list'),  # URL to get all registered users
    path('tasks/', TaskListView.as_view(), name='task_list'),  # URL for GET tasks
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),  # URL for POST create task
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),  # Update an existing task by pk
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),  # Delete a task by pk
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]