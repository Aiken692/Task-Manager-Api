from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from rest_framework.permissions import IsAuthenticated

class RegisterUserView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not (username and email and password):
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'id': user.id, 'username': user.username, 'email': user.email}, status=status.HTTP_201_CREATED)


# Create a view to fetch tasks
class TaskListView(APIView):
    permission_classes = [IsAuthenticated] # Require authentication for this view

    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        data = [
            {
                'id': task.id,
                'title': task.title,
                'description': task.description,
                'is_complete': task.is_complete,
                'deadline': task.deadline,
            } for task in tasks
        ]
        return Response(data)
