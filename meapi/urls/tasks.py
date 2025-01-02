from django.urls import path

from ..views.projects import PrivateMeProjectList, PrivateMeProjectDetails
from ..views.tasks import PrivateMeTaskCommentList

urlpatterns = [
    path(r"/<int:id>/comments/<int:comment_id>", PrivateMeTaskCommentList.as_view(), name="projectio.project-list"),
    path(r"/<int:id>/comments", PrivateMeTaskCommentList.as_view(), name="projectio.project-list"),
]
