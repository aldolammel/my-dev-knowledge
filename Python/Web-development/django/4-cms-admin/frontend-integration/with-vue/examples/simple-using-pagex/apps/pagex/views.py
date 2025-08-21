# FILE: /my_django_project/apps/pagex/views.py

#...
from rest_framework import viewsets
from .serializers import PageSerializer, CategorySerializer

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    """Used by Vue Router"""
    queryset = Page.objects.filter(is_published=True)
    serializer_class = PageSerializer
    lookup_field = 'id'
    

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Used by Vue Router"""
    queryset = PageCategory.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


#...
