from django.urls import path
from .views import (
    user_login,
    user_logout,
    user_signup,
    view_my_profile,
    view_user_profile,
    edit_user_profile,
)

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("signup/", user_signup, name="signup"),
    path("user-profile/mine/", view_my_profile, name="view_my_profile"),
    path("user-profile/<int:id>/", view_user_profile, name="view_user_profile"),
    path("user-profile/edit/", edit_user_profile, name="edit_user_profile"),
]
