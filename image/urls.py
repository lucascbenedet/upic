from django.urls import path
from .views import home, render_image, post_image_component, like_photo, delete_comment

app_name = "image"

urlpatterns = [
    path("", home, name="home"),
    path("home/", home, name="home"),
    path("<int:image_id>/", render_image, name="render_image"),
    path("post_image/", post_image_component, name="post_image"),
    path("like/<int:post_id>/", like_photo),
    path("delete-comment/<int:comment_id>/", delete_comment, name="delete_comment"),
]
