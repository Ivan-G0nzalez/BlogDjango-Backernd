from rest_framework import serializers
from .models import Post

class CategorySerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')

    class Meta:
        model = Post
        field = [
            'id',
            'name',
            'thumbnail',
        ]   