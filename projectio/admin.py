from django.contrib import admin

from .models import Project, ProjectMember


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ["uid", "name", "status", "created_at"]
    search_fields = list_display
    list_filter = ["status", "created_at"]
    readonly_fields = ["uid", "slug"]


@admin.register(ProjectMember)
class ProjectMemberAdmin(admin.ModelAdmin):
    model = ProjectMember
    list_display = ["uid", "role", "created_at"]
    search_fields = list_display + ["user__uid", "user__slug"]
    list_filter = ["role", "user__uid", "user__slug", "created_at"]
    readonly_fields = ["uid", "slug"]
