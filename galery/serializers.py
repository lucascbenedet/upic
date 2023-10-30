from rest_framework.serializers import ModelSerializer
from .models import Galery

class GallerySerializer(ModelSerializer):
    class Meta:
        model = Galery
        fields = '__all__'