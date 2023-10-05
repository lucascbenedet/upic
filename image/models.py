from django.db import models
from django.contrib.auth.models import User

class Image(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'image'

    def add_like(self,user):
        self.like.add(user)

    
class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    class Meta:
        db_table = 'like'

class Comment(models.Model):
    text = models.CharField(max_length=255)
    posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ForeignKey(Image,on_delete=models.CASCADE)

    class Meta:
        db_table = 'comment'

