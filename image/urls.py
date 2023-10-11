from django.urls import path
from django.urls import path, include

from .views import home,render_image,post_image_component





urlpatterns = [
    #path('', post, name='post'),
    path('home/', home),
    path('<int:image_id>/', render_image),
    path('post_image/', post_image_component),

]