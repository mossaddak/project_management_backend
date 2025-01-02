from rest_framework.serializers import ModelSerializer

from ..models import Comment


class CommentBaseSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = [
            "kind",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class PriateCommentSlimSerializer(CommentBaseSerializer):
    class Meta:
        model = CommentBaseSerializer.Meta.model
        fields = ["id"] + CommentBaseSerializer.Meta.fields


class PublicCommentSlimSerializer(CommentBaseSerializer):
    class Meta:
        model = CommentBaseSerializer.Meta.model
        fields = ["slug"] + CommentBaseSerializer.Meta.fields
