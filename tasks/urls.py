from django.urls import path
from django.http import HttpResponse
from .views import RegisterUserView, TaskListView, TaskCreateView, UserListView, TaskUpdateView, TaskDeleteView
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    # HTML response providing a better introduction to the API and available endpoints
    html_content = """
    <html>
        <head><title>Welcome to the Task Manager API</title></head>
        <body>
            <h1>Welcome to the Task Manager API</h1>
            <p>This API allows you to manage tasks and users. Below are the available endpoints:</p>
            <ul>
                <li><strong><a href="/register/">/register/</a></strong> - Register a new user</li>
                <li><strong><a href="/users/">/users/</a></strong> - List all users</li>
                <li><strong><a href="/tasks/">/tasks/</a></strong> - Get a list of tasks</li>
                <li><strong><a href="/tasks/create/">/tasks/create/</a></strong> - Create a new task</li>
                <li><strong>/tasks/&lt;int:pk&gt;/</strong> - Update an existing task by ID</li>
                <li><strong>/tasks/delete/&lt;int:pk&gt;/</strong> - Delete a task by ID</li>
                <li><strong><a href="/api/token/">/api/token/</a></strong> - Obtain a new authentication token</li>
                <li><strong><a href="/api/token/refresh/">/api/token/refresh/</a></strong> - Refresh the authentication token</li>
            </ul>
            <p>For more information, please refer to the API documentation.</p>
        </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('users/', UserListView.as_view(), name='user_list'),  # URL to get all registered users
    path('tasks/', TaskListView.as_view(), name='task_list'),  # URL for GET tasks
    path('tasks/create/', TaskCreateView.as_view(), name='task_create'),  # URL for POST create task
    path('tasks/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),  # Update an existing task by pk
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view(), name='task_delete'),  # Delete a task by pk
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]