
"""
    DJANGO SERIALIZERS > API LOGIC: DEFINING A VIEWSET

    Views are the place where all Django data is declared to be sent externally.

    >> Whole Django serialization roadmap:
        /Python/Web-development/django/3-2-views-and-API/serializer.txt
"""

# FILE: /apps/my_app/views.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from rest_framework import viewsets

class ExampleModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Sending JSON to the front-end."""
    
    queryset = ExampleModel.objects.prefetch_related("one_related_field_from_foreignkey")
    serializer_class = ExampleModelSerializer
    lookup_field = "slug"

    def get_queryset(self):
        """Built-in method to customize even more the qs."""
        return ExampleModel.objects.filter(is_published=True)