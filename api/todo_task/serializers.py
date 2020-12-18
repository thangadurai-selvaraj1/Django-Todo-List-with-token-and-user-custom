from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'task_name', 'owner', 'description',
                  'priority'
                  ]

    def validate(self, attrs):
        task_name = attrs.get('task_name' '')
        description = attrs.get('description' '')
        priority = attrs.get('priority' '')
        if len(task_name) < 2:
            raise serializers.ValidationError({'task_name': 'task_name min 3 char'})

        if description == '':
            raise serializers.ValidationError({'description': 'description cannot be empty'})

        if priority == '':
            raise serializers.ValidationError({'priority': 'priority cannot be empty'})

        return super().validate(attrs)
