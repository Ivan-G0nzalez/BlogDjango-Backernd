from rest_framework import serializers
from .models import Post
from apps.category.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    thumbnail = serializers.CharField(source='get_thumbnail')
    video = serializers.CharField(source='get_video')
    caterogy = CategorySerializer()
    class Meta:
        model = Post
        field = [
            'blog_uuid',
            'title',
            'slug',
            'thumbnail',
            'video',
            'description',
            'excerpt',
            'author',
            'category',
            'published',
            'status',
        ]