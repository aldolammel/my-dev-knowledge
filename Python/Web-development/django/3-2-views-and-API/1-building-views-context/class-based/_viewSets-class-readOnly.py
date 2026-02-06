
"""
    VIEWSETS > CLASS-BASED: USING READ-ONLY-MODEL

    >> With a basic view inherit, xxxxxxxxxxxxxxxxxxxxxxxx!

    >> It handles the xxxxxxxxxxxxxxxxxxxxxx

    >> Perfect when you need to xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
"""

# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# apps/my_app/models.py:
class ExampleModel(...):
    ...

# apps/my_app/serializers.py:
class ExampleModelSerializer(...):
    ...

# apps/my_app/views.py:
from django.views import View

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