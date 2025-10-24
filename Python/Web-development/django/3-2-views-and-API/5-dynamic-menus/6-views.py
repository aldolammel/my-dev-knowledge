from rest_framework import viewsets

from .models import (
    PagexMenu,
)
from .serializers import (
    PagexMenuSerializer,
)


class PagexMenuViewSet(viewsets.ReadOnlyModelViewSet):
    """Sending data to Vue Router"""

    queryset = PagexMenu.objects.prefetch_related("links")
    serializer_class = PagexMenuSerializer
    lookup_field = "identifier"
