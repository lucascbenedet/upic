from django.db import models
from image.models import Image
from django.contrib.auth.models import User

class Galery(models.Model):
    name = models.CharField(max_length=30)
    image = models.ManyToManyField(Image)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


