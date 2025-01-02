from django.db import models


class TaskStatusChoices(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    TODO = "TODO", "To Do"
    In_PROGRESS = "In_PROGRESS", "In progress"
    DONE = "DONE", "Done"
    REMOVED = "REMOVED", "Removed"


class TaskPriorityChoices(models.TextChoices):
    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM", "Medium"
    HIGH = "HIGH", "High"
