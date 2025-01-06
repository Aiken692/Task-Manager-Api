from django.urls import path
from django.http import HttpResponse
from .views import RegisterUserView, TaskListView, TaskCreateView, UserListView, TaskUpdateView, TaskDeleteView
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    # HTML response with refined styling
    html_content = """
    <html>
        <head>
            <title>Task Manager API</title>
            <style>
                body {
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    text-align: center;
                    margin-top: 100px;
                    background-color: #f4f7f6;
                }
                h1 {
                    font-size: 60px;
                    color: #333;
                    margin-bottom: 20px;
                    font-weight: bold;
                }
                p {
                    font-size: 20px;
                    color: #555;
                }
                a {
                    font-size: 25px;
                    color: black;
                    text-decoration: none;
                    padding: 12px 24px;
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    border: 1px solid #ddd;
                    transition: background-color 0.3s, color 0.3s;
                }
                a:hover {
                    background-color: #007BFF;
                    color: white;
                }
                .container {
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Task Manager API</h1>
                <p>Welcome to the Task Manager API! You can manage tasks and users through the API.</p>
                <p><a href="http://localhost:8000/swagger/">Documentation</a></p>
            </div>
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