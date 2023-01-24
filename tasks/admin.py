from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "due_date",
        "project",
        "assignee",
        "is_completed",
    )
