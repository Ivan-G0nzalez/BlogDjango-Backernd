from django.urls import path

from .views import *

urlpatterns = [
    path('categories', ListCategoryView.as_view()),
]
