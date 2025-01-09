from django.urls import path
from django.http import HttpResponse
from .views import RegisterUserView, TaskListView, TaskCreateView, UserListView, TaskUpdateView, TaskDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    # HTML content for the landing page
    html_content = f"""
    <html>
        <head>
            <title>Task Manager API</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    text-align: center;
                    margin-top: 100px;
                    background-color: #f4f7f6;
                }}
                h1 {{
                    font-size: 60px;
                    color: #333;
                    margin-bottom: 20px;
                    font-weight: bold;
                }}
                p {{
                    font-size: 20px;
                    color: #555;
                }}
                a {{
                    font-size: 16px;
                    color: #007BFF;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                table {{
                    width: 60%;
                    margin: 20px auto;
                    border-collapse: collapse;
                }}
                th, td {{
                    text-align: left;
                    padding: 12px;
                    border: 1px solid #ddd;
                }}
                th {{
                    background-color: #f8f9fa;
                    font-size: 18px;
                    color: #333;
                }}
                td {{
                    font-size: 16px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Task Manager API</h1>
                <p>Welcome to the Task Manager API! You can manage tasks and users through the API.</p>
                <p>Documentation</p>
                <table>
                    <tr>
                        <th>URL</th>
                        <th>Description</th>
                    </tr>
                    <tr>
                        <td><a href="/register/">Register User</a></td>
                        <td>/register</td>
                    </tr>
                    <tr>
                        <td><a href="/users/">List Users</a></td>
                        <td>/users</td>
                    </tr>
                    <tr>
                        <td><a href="/tasks/">List Tasks</a></td>
                        <td>/tasks</td>
                    </tr>
                    <tr>
                        <td><a href="/tasks/create/">Create Task</a></td>
                        <td>/tasks/create</td>
                    </tr>
                    <tr>
                        <td>Update Task</td>
                        <td>/tasks/id</td>
                    </tr>
                    <tr>
                        <td>Delete Task</td>
                        <td>/tasks/delete/id</td>
                    </tr>
                    <tr>
                        <td><a href="/api/token/">Obtain Token</a></td>
                        <td>/api/token/</td>
                    </tr>
                    <tr>
                        <td><a href="/api/token/refresh/">Refresh Token</a></td>
                        <td>/api/token/refresh/</td>
                    </tr>
                    <tr>
                        <td><a href="/login/">Login</a></td>
                        <td>/login/</td>
                    </tr>
                </table>
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
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Add this line for the login URL
]