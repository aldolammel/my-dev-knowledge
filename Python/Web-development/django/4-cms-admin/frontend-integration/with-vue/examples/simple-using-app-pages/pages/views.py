# FILE: /my_django_project/pages/views.py

#...
from rest_framework import viewsets
from .serializers import PageSerializer, CategorySerializer

class PageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Page.objects.filter(is_published=True)
    serializer_class = PageSerializer
    lookup_field = 'id'
    

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PageCategory.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


#...
