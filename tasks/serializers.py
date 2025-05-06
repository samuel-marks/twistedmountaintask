from rest_framework import serializers

from .models import Task  # Replace with your actual model name

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'  # You can specify fields explicitly, e.g., ['field1', 'field2']
        read_only_fields = ['assigned_to', 'created_at']
