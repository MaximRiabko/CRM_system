from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    RegisterUser,
    ProfileUser,
    LogoutView,
)

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="users/login.html",
        redirect_authenticated_user=True,
    ),
         name="login"),
    path("register/", RegisterUser.as_view(), name="register"),
    path("about_me/", ProfileUser.as_view(), name="about_me"),
    path("logout/", LogoutView.as_view(), name="logout"),
]