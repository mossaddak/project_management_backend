from rest_framework.serializers import Serializer, ModelSerializer

from accountio.serializers.common import PriateUserSlimSerializer

from projectio.serializers.common import ProjectBaseSerializer


class PrivateMeProjectListSerializer(ProjectBaseSerializer):
    class Meta:
        model = ProjectBaseSerializer.Meta.model
        fields = ["id"] + ProjectBaseSerializer.Meta.fields

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super().create(validated_data)


class PrivateMeProjectDetailsSerializer(ProjectBaseSerializer):
    class Meta:
        model = ProjectBaseSerializer.Meta.model
        fields = ["id"] + ProjectBaseSerializer.Meta.fields
