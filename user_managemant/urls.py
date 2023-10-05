from django.urls import path
from .login_views import login,register

urlpatterns = [
    path('login/', login),
    path('register/',register)
]