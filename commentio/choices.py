from django.db import models


class CommentStatusChoices(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PENDING = "PENDING", "Pending"
    PUBLISHED = "PUBLISHED", "Published"
    REMOVED = "REMOVED", "Removed"


class CommentKindChoices(models.TextChoices):
    TASK = "TASK", "Task"
    PROJECT = "PROJECT", "Project"
