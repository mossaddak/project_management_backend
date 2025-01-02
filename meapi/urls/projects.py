from django.urls import path

from ..views.projects import PrivateMeProjectList, PrivateMeProjectDetails
from ..views.tasks import PrivateMeTaskList, PrivateMeTaskDetails

urlpatterns = [
    path(
        r"/<int:id>/tasks/<int:task_id>",
        PrivateMeTaskDetails.as_view(),
        name="projectio.project-task-details",
    ),
    path(
        r"/<int:id>/tasks",
        PrivateMeTaskList.as_view(),
        name="projectio.project-task-list",
    ),
    path(
        r"/<int:id>",
        PrivateMeProjectDetails.as_view(),
        name="projectio.project-details",
    ),
    path(r"", PrivateMeProjectList.as_view(), name="projectio.project-list"),
]
