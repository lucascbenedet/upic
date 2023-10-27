from django.urls import path
from .views import render_gallery

app_name = 'gallery'
urlpatterns = [
    path('gallery/', render_gallery, name='render_gallery')
]