
"""
    VIEWSETS > CLASS-BASED: USING READ-ONLY-MODEL

    >> With a basic view inherit, xxxxxxxxxxxxxxxxxxxxxxxx!

    >> It handles the xxxxxxxxxxxxxxxxxxxxxx

    >> Perfect when you need to xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
"""

# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# apps/subapp/models.py:
class ExampleModel(...):
    ...

# apps/subapp/serializers.py:
class ExampleModelSerializer(...):
    ...

# apps/subapp/views.py:
from rest_framework import viewsets
from . import models
from . import serializers as serial

class ExampleModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoint exposing XXXXXXXXXXXXXXXXX to <<<<<<<Vue Router>>>>>."""

    queryset = models.ExampleModel.objects.filter(is_published=True).prefetch_related(
        "categories",
        "seo_keywords",
    )
    serializer_class = serial.ExampleModelSerializer
    lookup_field = "slug"  # Allow lookup by other attr. instead of ID.
    lookup_value_regex = "[^/]+"  # Handles slugs with hyphens or underscores correctly.


"""
    HOW TO USE (EXAMPLE):
        ./xxxxxxxxxxxxxxxxx

    WHO INHERIT VIEW CLASS:
        >> xxxxxxxxxxxxxxxxxxxxxxxx
"""