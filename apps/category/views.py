from django.shortcuts import render

from apps.category.serializers import CategorySerializer
from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import Category
from rest_framework.pagination import PageNumberPagination

# Create your views here.
class ListCategory(APIView):
    def get(self, request, format=None):
        if Category.objects.all().exists():
            categories = Category.objects.all()
            result = []
            for category in categories:
                if not category.parent:
                    item = {}
                    item['id'] = category.id
                    item['name'] = category.name
                    item['thumbnail'] = category.thumbnail.url
                
                for cat in categories:
                    sub_item = {}    
                    if cat.parent and cat.parent.id == category.id:
                        sub_item['id'] = cat.id 
                        sub_item = cat.name
                        sub_item['thumbnail'] = cat.thumbnail.url
                        item['sub_category'].append(sub_item)
                
                result.append(item)        
                    
            return Response({'category': 'result'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No category Found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    
