from django.urls import path
from django.urls import path, include

from .views import image_view,home





urlpatterns = [
    #path('', post, name='post'),
    path('view/', image_view),
    path('home/', home),

]