
"""
    DJANGO SERIALIZERS: DEFINING THE API LOGIC THROUGH A VIEWSET

    Views are the place where all Django data is declared to be sent externally.

    >> Whole Django serialization roadmap:
        ./serializer.txt

    >> Or if you just want to a simple serializer class model:
        ./_serializer-class-model.py
"""

# FILE: /apps/my_app/views.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
from rest_framework import viewsets
from . import models
from . import serializers as serial

class ExampleModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoint exposing XXXXXXXXXXXXXXXXX to Vue Router."""
    
    queryset = models.ExampleModel.objects.prefetch_related("one_related_field_from_foreignkey")
    serializer_class = serial.ExampleModelSerializer
    lookup_field = "slug"

    def get_queryset(self):
        """Built-in method to customize even more the qs."""
        return models.ExampleModel.objects.filter(is_published=True)