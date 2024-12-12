from django.urls import path
from .views import TaskListView, RegisterUserView
from django.http import HttpResponse
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

def home(request):
    return HttpResponse("Welcome to the Task Manager!")

urlpatterns = [
    path('', home, name='home'),  # Add this line for the root URL
    path('register/', RegisterUserView.as_view(), name='register'),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]