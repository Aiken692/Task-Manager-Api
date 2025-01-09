from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .models import Task
from .serializers import TaskSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterUserView(APIView):
    permission_classes = [AllowAny]  # Allow any user to access this view

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not (username and email and password):
            return Response({'error': 'All fields are required.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({'error': 'Email is already registered.'}, 
            status=status.HTTP_400_BAD_REQUEST
        )

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Create JWT token
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)

        return Response(
            {'id': user.id, 'username': user.username, 'email': user.email, 'access_token': access_token}, 
            status=status.HTTP_201_CREATED
        )

class UserListView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication for this view

    def get(self, request):
        users = User.objects.all()  # Get all users
        user_data = [{"id": user.id, "username": user.username, "email": user.email} for user in users] # Serialize user data into a list of dictionaries
        return Response(user_data, status=status.HTTP_200_OK) # Return the serialized user data

# Create a view to fetch tasks for the authenticated user
class TaskListView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def get(self, request):
        # Get all tasks for the currently authenticated user
        tasks = Task.objects.filter(user=request.user)
        
        # Serialize the task data into JSON format
        serializer = TaskSerializer(tasks, many=True)
        
        # Return the serialized task data
        return Response(serializer.data)



class TaskCreateView(APIView):
    permission_classes = [IsAuthenticated]  # Require authentication for this view

    def post(self, request):
        serializer = TaskSerializer(data=request.data) # Serialize the incoming data
        if serializer.is_valid(): # Validate the data (ensure it's correct and complete)
            serializer.save(user=request.user)  # Set the user to the authenticated user
            return Response(serializer.data, status=status.HTTP_201_CREATED)# Return the serialized task data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)# If validation fails, return errors

# Create a view to update and delete tasks
# api/views.py
class TaskUpdateView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def put(self, request, pk):
        # Get the task by primary key (pk), ensuring it belongs to the authenticated user
        task = Task.objects.get(pk=pk, user=request.user)
        
        # Serialize the data, using the existing task to update
        serializer = TaskSerializer(task, data=request.data)
        
        # Validate the updated data
        if serializer.is_valid():
            # Save the updated task
            serializer.save()
            # Return the updated task data
            return Response(serializer.data)
        
        # If validation fails, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDeleteView(APIView):
    permission_classes = [IsAuthenticated]  # Ensure the user is authenticated

    def delete(self, request, pk):
        try:
            # Get the task by primary key (pk), ensuring it belongs to the authenticated user
            task = Task.objects.get(pk=pk, user=request.user)
            # Delete the task from the database
            task.delete()
            # Return a success message with no content
            return Response({"message": "Task deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            # Return an error if the task does not exist
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            # Log the exception and return a generic error response
            print(f"Error: {e}")
            return Response({"error": "An error occurred."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
