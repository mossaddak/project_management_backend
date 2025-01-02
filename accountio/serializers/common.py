from versatileimagefield.serializers import VersatileImageFieldSerializer

from rest_framework.serializers import ModelSerializer

from ..models import User


class UserBaseSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["created_at", "updated_at"]


class PriateUserSlimSerializer(UserBaseSerializer):
    class Meta:
        model = UserBaseSerializer.Meta.model
        fields = ["id"] + UserBaseSerializer.Meta.fields


class PublicUserSlimSerializer(UserBaseSerializer):
    class Meta:
        model = UserBaseSerializer.Meta.model
        fields = ["slug"] + UserBaseSerializer.Meta.fields
