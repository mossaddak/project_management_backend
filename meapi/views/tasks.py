from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)

from commentio.models import Comment

from taskio.models import Task

from projectio.models import Project

from ..serializers.tasks import (
    PrivateMeTaskListSerializer,
    PrivateMeTaskDetailsSerializer,
    PrivateMeTaskCommentListserializer,
)


class PrivateMeTaskList(ListCreateAPIView):
    serializer_class = PrivateMeTaskListSerializer

    def get_queryset(self):
        return Task.objects.filter(
            project=get_object_or_404(
                Project.objects.filter(id=self.kwargs.get("id", None))
            )
        ).select_related("assigned_to")


class PrivateMeTaskDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PrivateMeTaskDetailsSerializer

    def get_object(self):
        return get_object_or_404(
            Task.objects.filter(
                project=get_object_or_404(
                    Project.objects.filter(id=self.kwargs.get("id", None))
                )
            ),
            id=self.kwargs.get("task_id", None),
        )


class PrivateMeTaskCommentList(ListCreateAPIView):
    serializer_class = PrivateMeTaskCommentListserializer

    def get_queryset(self):
        return Comment.objects.filter(
            task=get_object_or_404(Task.objects.filter(id=self.kwargs.get("id", None)))
        ).select_related("task", "user")


class PrivateMeTaskCommentDetails(ListCreateAPIView):
    serializer_class = PrivateMeTaskCommentListserializer

    def get_object(self):
        return get_object_or_404(
            Comment.objects.filter(
                task=get_object_or_404(
                    Task.objects.filter(id=self.kwargs.get("id", None))
                ),
                id=self.kwargs.get("comment_id", None),
            ).select_related("task", "user")
        )
