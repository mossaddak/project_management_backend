from django.db import models

class UserStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    ACTIVE = "ACTIVE", "Active"
    PENDING = "PENDING", "Pending"
    DISABLED = "DISABLED", "Disabled"