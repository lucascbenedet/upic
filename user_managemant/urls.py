from django.urls import path
from .views import user_login, register, profile, user_logout, alter_user

app_name = "auth"

urlpatterns = [
    path("log-in/", user_login, name="user_login"),
    path("register/", register, name="register"),
    path("profile/<str:username>/", profile, name="profile"),
    path("logout/", user_logout, name="user_logout"),
    path("alter_user/", alter_user, name="alter_user"),
]
