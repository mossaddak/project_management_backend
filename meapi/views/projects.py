from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)

from ..serializers.projects import (
    PrivateMeProjectListSerializer,
    PrivateMeProjectDetailsSerializer,
)

from projectio.models import Project


class PrivateMeProjectList(ListCreateAPIView):
    serializer_class = PrivateMeProjectListSerializer

    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)


class PrivateMeProjectDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMeProjectDetailsSerializer

    def get_object(self):
        return get_object_or_404(
            Project.objects.filter(
                owner=self.request.user, id=self.kwargs.get("id", None)
            )
        )
