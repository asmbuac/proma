from django.urls import path
from .views import create_task, task_list

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", task_list, name="show_my_tasks"),
]
