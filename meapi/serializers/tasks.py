from rest_framework.generics import get_object_or_404
from rest_framework.serializers import SlugRelatedField

from accountio.serializers.common import (
    PriateUserSlimSerializer,
    PublicUserSlimSerializer,
)
from accountio.choices import UserStatus
from accountio.models import User

from commentio.choices import CommentStatusChoices, CommentKindChoices
from commentio.serializers.common import CommentBaseSerializer

from taskio.serializers.common import TaskBaseSerializer

from projectio.models import Project

from taskio.serializers.common import TaskProjectSlimSerializer
from taskio.models import Task


class PrivateMeTaskListSerializer(TaskBaseSerializer):
    assignee_id = SlugRelatedField(
        queryset=User.objects.filter(status=UserStatus.ACTIVE),
        slug_field="id",
        write_only=True,
    )
    assigned_to = PriateUserSlimSerializer(read_only=True)

    class Meta:
        model = TaskBaseSerializer.Meta.model
        fields = ["id", "assigned_to", "assignee_id"] + TaskBaseSerializer.Meta.fields

    def create(self, validated_data):
        validated_data["project"] = get_object_or_404(
            Project.objects.filter(id=self.context.get("view").kwargs.get("id", None))
        )
        validated_data["assigned_to"] = validated_data.pop("assignee_id")
        return super().create(validated_data)


class PrivateMeTaskDetailsSerializer(TaskBaseSerializer):
    assignee_id = SlugRelatedField(
        queryset=User.objects.filter(status=UserStatus.ACTIVE),
        slug_field="id",
        write_only=True,
    )
    assigned_to = PriateUserSlimSerializer(read_only=True)

    class Meta:
        model = TaskBaseSerializer.Meta.model
        fields = ["id", "assigned_to", "assignee_id"] + TaskBaseSerializer.Meta.fields

    def update(self, instance, validated_data):
        if project := get_object_or_404(
            Project.objects.filter(id=self.context.get("view").kwargs.get("id", None))
        ):
            validated_data["project"] = project
        if assignee_to := validated_data.pop("assignee_id"):
            validated_data["assigned_to"] = assignee_to
        return super().update(instance, validated_data)


class PrivateMeTaskCommentListserializer(CommentBaseSerializer):
    user = PublicUserSlimSerializer(read_only=True)

    class Meta:
        model = CommentBaseSerializer.Meta.model
        fields = [
            "id",
            "kind",
            "status",
            "user",
        ] + CommentBaseSerializer.Meta.fields
        read_only_fields = ["kind", "status"]

    def create(self, validated_data):
        validated_data["status"] = CommentStatusChoices.PUBLISHED
        validated_data["kind"] = CommentKindChoices.TASK
        validated_data["task"] = get_object_or_404(
            Task.objects.filter(id=self.context.get("view").kwargs.get("id", None))
        )
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class PrivateMeTaskCommentDetailsserializer(CommentBaseSerializer):
    user = PublicUserSlimSerializer(read_only=True)

    class Meta:
        model = CommentBaseSerializer.Meta.model
        fields = [
            "id",
            "kind",
            "status",
            "user",
        ] + CommentBaseSerializer.Meta.fields
        read_only_fields = ["kind", "status"]
