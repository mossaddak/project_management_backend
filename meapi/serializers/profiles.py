from versatileimagefield.serializers import VersatileImageFieldSerializer

from rest_framework.serializers import CharField

from django.contrib.auth.hashers import make_password
from django.db import transaction

from accountio.serializers.common import UserBaseSerializer


class MeProfileSerializer(UserBaseSerializer):
    password = CharField(write_only=True, min_length=8, required=False)
    class Meta:
        model = UserBaseSerializer.Meta.model
        fields = [
            "id",
            "email",
            "password",
        ] + UserBaseSerializer.Meta.fields
        read_only_fields = ["id", "status", "created_at", "updated_at"]
        extra_kwargs = {"password": {"write_only": True}}

    @transaction.atomic
    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        if password:
            validated_data["password"] = make_password(password)
        return super().update(instance, validated_data)
