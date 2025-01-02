from rest_framework.serializers import ModelSerializer

from ..models import Project


class ProjectBaseSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = [
            "name",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class PriateProjectSlimSerializer(ProjectBaseSerializer):
    class Meta:
        model = ProjectBaseSerializer.Meta.model
        fields = ["id"] + ProjectBaseSerializer.Meta.fields


class PublicProjectSlimSerializer(ProjectBaseSerializer):
    class Meta:
        model = ProjectBaseSerializer.Meta.model
        fields = ["slug"] + ProjectBaseSerializer.Meta.fields
