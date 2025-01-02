from rest_framework.serializers import ModelSerializer

from ..models import Task


class TaskBaseSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = [
            "status",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class TaskProjectSlimSerializer(TaskBaseSerializer):
    class Meta:
        model = TaskBaseSerializer.Meta.model
        fields = ["id"] + TaskBaseSerializer.Meta.fields


class TaskProjectSlimSerializer(TaskBaseSerializer):
    class Meta:
        model = TaskBaseSerializer.Meta.model
        fields = ["slug"] + TaskBaseSerializer.Meta.fields
