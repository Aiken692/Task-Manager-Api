from django.urls import path
from .views import TaskListView, RegisterUserView
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Task Manager!")

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('register/', RegisterUserView.as_view(), name='register'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
]