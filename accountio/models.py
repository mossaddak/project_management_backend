from autoslug import AutoSlugField

from versatileimagefield.fields import VersatileImageField

from django.contrib.auth.models import AbstractUser
from django.db import models

from common.models import BaseModelWithUID

from .choices import UserStatus
from .helpers.media_path import get_user_media_path_prefix
from .helpers.slug_helpers import get_user_slug 
from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser, BaseModelWithUID):
    slug = AutoSlugField(populate_from=get_user_slug, unique=True, db_index=True)
    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField(unique=True, db_index=True)
    status = models.CharField(
        max_length=20,
        choices=UserStatus,
        db_index=True,
        default=UserStatus.PENDING,
    )
    avatar = VersatileImageField(
        "Avatar",
        upload_to=get_user_media_path_prefix,
        blank=True,
    )
    joined_date = models.DateTimeField(auto_now_add=True)
    objects = CustomUserManager()
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        ordering = ("-date_joined",)

    def __str__(self):
        return f"ID: {self.id}, Username: {self.username}"

    @property
    def full_name(self):
        return (
            f"{self.first_name} {self.last_name}"
            if self.first_name or self.last_name
            else self.username.capitalize()
        )