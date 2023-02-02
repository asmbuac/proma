from django.urls import path
from .views import create_task, list_tasks, delete_task, edit_task

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", list_tasks, name="show_my_tasks"),
    path("<int:id>/delete/", delete_task, name="delete_task"),
    path("<int:id>/edit/", edit_task, name="edit_task"),
]
