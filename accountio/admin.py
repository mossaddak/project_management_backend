from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ["uid", "slug", "status", "created_at"]
    search_fields = list_display
    list_filter = ["status", "created_at"]
    readonly_fields = ["uid", "slug"]
