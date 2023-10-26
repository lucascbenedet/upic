from django.urls import path
from .views import user_login,register,profile,user_logout

app_name = 'auth'

urlpatterns = [
    path('log-in/', user_login, name='user_login'),
    path('register/',register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/',user_logout, name='user_logout' )
]