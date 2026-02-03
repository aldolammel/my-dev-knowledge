
"""
    VIEWSETS > CLASS-BASED: USING READ-ONLY-MODEL

    >> With a basic view inherit, xxxxxxxxxxxxxxxxxxxxxxxx!

    >> It handles the xxxxxxxxxxxxxxxxxxxxxx

    >> Perfect when you need to xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.
"""

# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views import View


class PagexPostViewSet(viewsets.ReadOnlyModelViewSet):
    """Read-only endpoint exposing published posts to Vue Router."""

    queryset = models.PagexPost.objects.filter(is_published=True).prefetch_related(
        "categories",
        "seo_keywords",
    )
    serializer_class = serial.PagexPostSerializer
    lookup_field = "slug"  # Allow lookup by other attr. instead of ID.
    lookup_value_regex = "[^/]+"  # Handles slugs with hyphens or underscores correctly.


"""
    HOW TO USE (EXAMPLE):
        ./xxxxxxxxxxxxxxxxx

    WHO INHERIT VIEW CLASS:
        >> xxxxxxxxxxxxxxxxxxxxxxxx
"""