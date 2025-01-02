from django.contrib import admin

from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ["uid", "status", "priority", "due_date", "created_at"]
    search_fields = list_display
    list_filter = ["status", "priority", "due_date", "created_at"]
    readonly_fields = ["uid", "slug"]
