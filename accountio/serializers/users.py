from django.db import transaction

from rest_framework.serializers import (
    CharField,
    SlugRelatedField,
    Serializer,
    ValidationError,
)

from ..choices import UserStatus
from ..models import User
from ..helpers.token_helpers import get_token

from .common import UserBaseSerializer


class UserRegisterSerializer(UserBaseSerializer):
    class Meta:
        model = UserBaseSerializer.Meta.model
        fields = [
            "id",
            "email",
            "joined_date",
            "password",
        ] + UserBaseSerializer.Meta.fields
        read_only_fields = ["id", "status", "joined_date", "created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}

    @transaction.atomic
    def create(self, validated_data):
        validated_data["kind"] = UserStatus.ACTIVE
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return validated_data


class UserListSerializer(UserBaseSerializer):
    class Meta:
        model = UserBaseSerializer.Meta.model
        fields = ["id", "email", "joined_date"] + UserBaseSerializer.Meta.fields
        read_only_fields = ["id", "status", "created_at", "updated_at"]


class UserLoginSerializer(Serializer):
    username = SlugRelatedField(
        queryset=User.objects.all(), slug_field="username", write_only=True
    )
    password = CharField(write_only=True)
    refresh = CharField(max_length=255, read_only=True)
    access = CharField(max_length=255, read_only=True)

    def validate(self, validated_data):
        username = validated_data.get("username")
        password = validated_data.get("password")
        try:
            user = User.objects.get(username=username.username)
        except User.DoesNotExist:
            raise ValidationError({"detail": "Invalid credential!"})

        if not user.check_password(password):
            raise ValidationError({"detail": "Invalid credential!"})

        validated_data["refresh"], validated_data["access"] = get_token(user)
        return validated_data

    def create(self, validated_data):
        return validated_data
