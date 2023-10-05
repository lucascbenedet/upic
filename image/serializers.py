from rest_framework.serializers import ModelSerializer
from .models import Image, Like,Comment

class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class ListCommentsSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user_id', 'text']