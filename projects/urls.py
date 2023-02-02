from django.urls import path
from .views import list_all_projects, list_my_projects, show_project, create_project

urlpatterns = [
    path("", list_all_projects, name="list_all_projects"),
    path("mine/", list_my_projects, name="list_my_projects"),
    path("<int:id>/", show_project, name="show_project"),
    path("create/", create_project, name="create_project"),
]
