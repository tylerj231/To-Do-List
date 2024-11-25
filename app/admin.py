from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from app.models import User, Task, Tag


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "first_name",
        "last_name",
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                    )
                },
            ),
        )
    )


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content",
        "created",
        "deadline",
        "status",
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
