from django.urls import path
from .views import render_gallery,gallery_page,create_gallery,delete_gallery

app_name = 'gallery'
urlpatterns = [
    path('', gallery_page, name='gallery-page'),
    path('<int:pk>/', render_gallery,name='render-gallery'),
    path('create/', create_gallery,name='create-gallery'),
    path('<int:pk>',delete_gallery,name='delete-gallery')
]