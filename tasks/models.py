from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# User model is provided by Django's built-in authentication system, so we only need to define the Task model.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_complete = models.BooleanField(default=False)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.title