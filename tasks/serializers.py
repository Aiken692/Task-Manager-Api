from rest_framework import serializers
from .models import Task

# Serializer to convert Task model data to JSON format and vice versa
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at', 'user']

    def validate_due_date(self, value):
        if value and value <= timezone.now().date():
            raise serializers.ValidationError("The due date must be in the future.")
        return value


# In this serializer:

# fields: Specifies which fields will be included in the serialized data.
# read_only_fields: Fields that cannot be updated directly by the user. These include the id, created_at, updated_at, and user.
# validate_due_date: A custom validator to ensure that the due_date is always in the future.