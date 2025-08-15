# FILE: /my_django_project/pages/serializers.py

from rest_framework import serializers
from .models import Page, PageCategory

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = [
            'id', 
            'title', 
            'slug',
            'seo_title',
            'seo_desc',
            'content',
            'img_highlight',
            'categories',
        ]

class CategorySerializer(serializers.ModelSerializer):
    pages = PageSerializer(many=True, read_only=True)
    
    class Meta:
        model = PageCategory
        fields = [
            'id', 
            'cat',
            'slug',
            'pages',
        ]