from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ["uid", "status", "kind", "created_at"]
    search_fields = list_display
    list_filter = ["status", "kind", "created_at"]
    readonly_fields = ["uid", "slug"]
