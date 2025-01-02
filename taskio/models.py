from autoslug import AutoSlugField

from django.db import models

from common.models import BaseModelWithUID

from .choices import TaskStatusChoices, TaskPriorityChoices
from .helpers.slug_helpers import get_task_slug


class Task(BaseModelWithUID):
    slug = AutoSlugField(populate_from=get_task_slug, unique=True, db_index=True)
    status = models.CharField(
        max_length=20,
        choices=TaskStatusChoices,
        db_index=True,
        default=TaskStatusChoices.TODO,
    )
    priority = models.CharField(
        max_length=20,
        choices=TaskPriorityChoices,
        db_index=True,
        default=TaskPriorityChoices.LOW,
    )
    due_date = models.DateTimeField(blank=True, null=True)

    # FK
    assigned_to = models.ForeignKey("accountio.User", on_delete=models.CASCADE)
    project = models.ForeignKey("projectio.Project", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("project", "assigned_to")

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}"
