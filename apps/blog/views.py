from django.shortcuts import get_object_or_404, render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions


# Create your views here.

from .models import Post
from .serializers import PostSerializer
from .pagination import SmallPagination, MediumSetPagination, LargeSetPagination

class BlogListView(APIView):
    def get(self, request, format=None):
        if Post.objects.all().exists():
            post = Post.objects.all()
            
            paginator = SmallPagination()
            results = paginator.paginate_queryset(post,request)
            serializer = PostSerializer(results, many=True)
            
            return paginator.get_paginated_response({'post': serializer.data})
        else:
            return Response({"error": "No post found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class PostDetailsView(APIView):
    def get(self, request,post_slug ,format=None):
        post = get_object_or_404(Post, slug=post_slug)
        serializer = PostSerializer(post)
        return Response({"post": serializer.data}, status=status.HTTP_200_OK)        