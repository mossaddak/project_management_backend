from django.db import models


class ProjectStatusChoices(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PENDING = "PENDING", "Pending"
    ACTIVE = "ACTIVE", "Active"
    REMOVED = "REMOVED", "Removed"
    DISABLED = "DISABLED", "Disabled"


class ProjectMemberRoleChoices(models.TextChoices):
    ADMIN = "ADMIN", "Admin"
    MEMBER = "MEMBER", "Member"
