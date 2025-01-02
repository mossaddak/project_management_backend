from autoslug import AutoSlugField

from django.db import models

from common.models import BaseModelWithUID

from .choices import CommentStatusChoices, CommentKindChoices
from .helpers.slug_helpers import get_task_comment_slug


class Comment(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_task_comment_slug, unique=True, db_index=True
    )
    status = models.CharField(
        max_length=20, choices=CommentStatusChoices, default=CommentStatusChoices.DRAFT
    )
    kind = models.CharField(max_length=20, choices=CommentKindChoices)

    # FK
    task = models.ForeignKey("taskio.Task", on_delete=models.CASCADE)
    user = models.ForeignKey("accountio.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Task: {self.task.title}, User: {self.user.username}"
