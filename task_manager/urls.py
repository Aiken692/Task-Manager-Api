"""
URL configuration for task_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from django.http import HttpResponse

def home(request):
    # Manually list the URL patterns
    url_list = [
        request.build_absolute_uri('/register/'),
        request.build_absolute_uri('/users/'),
        request.build_absolute_uri('/tasks/'),
        request.build_absolute_uri('/tasks/create/'),
        '/tasks/id',  # Display as plain text
        '/tasks/delete/id',  # Display as plain text
        '/api/token/',  # Display as plain text
        '/api/token/refresh/',  # Display as plain text
    ]

    # Format the HTML content with the URL list in a table
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
                    font-size: 25px;
                    color: black;
                    text-decoration: none;
                    padding: 12px 24px;
                    background-color: #f8f9fa;
                    border-radius: 8px;
                    border: 1px solid #ddd;
                    transition: background-color 0.3s, color 0.3s;
                }}
                a:hover {{
                    background-color: #007BFF;
                    color: white;
                }}
                .container {{
                    max-width: 600px;
                    margin: 0 auto;
                    padding: 20px;
                    background-color: #ffffff;
                    border-radius: 12px;
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
                }}
                table {{
                    width: 100%;
                    margin-top: 20px;
                    border-collapse: collapse;
                }}
                th, td {{
                    padding: 10px;
                    border: 1px solid #ddd;
                    text-align: left;
                }}
                th {{
                    background-color: #f8f9fa;
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
                    </tr>
                    {"".join([f"<tr><td>{url if 'id' in url else f'<a href={url}>{url}</a>'}</td></tr>" for url in url_list])}
                </table>
            </div>
        </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include URLs from the tasks app
]
