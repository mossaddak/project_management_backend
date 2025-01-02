from autoslug import AutoSlugField

from django.db import models

from common.models import BaseModelWithUID

from .choices import ProjectStatusChoices, ProjectMemberRoleChoices
from .helpers.slug_helpers import get_project_slug, get_project_member_slug


class Project(BaseModelWithUID):
    slug = AutoSlugField(populate_from=get_project_slug, unique=True, db_index=True)
    name = models.CharField(max_length=100, unique=True)
    status = models.CharField(
        max_length=20,
        choices=ProjectStatusChoices,
        db_index=True,
        default=ProjectStatusChoices.DRAFT,
    )
    owner = models.ForeignKey("accountio.User", on_delete=models.CASCADE)

    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}"


class ProjectMember(BaseModelWithUID):
    slug = AutoSlugField(
        populate_from=get_project_member_slug, unique=True, db_index=True
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey("accountio.User", on_delete=models.CASCADE)
    role = models.CharField(
        choices=ProjectMemberRoleChoices,
        default=ProjectMemberRoleChoices.MEMBER,
        max_length=20,
    )

    class Meta:
        unique_together = ("project", "user")

    def __str__(self):
        return (
            f"ID: {self.id}, Project: {self.project.title}, User: {self.user.username}"
        )
