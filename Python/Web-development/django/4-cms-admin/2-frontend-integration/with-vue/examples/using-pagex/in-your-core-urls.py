# THIS FILE IS YOUR /PROJECT_DJANGO/CORE/URLS.PY:

from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView

from .settings import (
    DEBUG,
    MEDIA_ROOT,
    MEDIA_URL,
    STATIC_ROOT,
    STATIC_URL,
)

urlpatterns = [
    # DJANGO:
    ...
    # APIs:
    path("api/", include("apps.pagex.urls")),  # needs to be before the Vue fallback!
    # FRONTEND:
    # Only under development:
    # reserved space...
    # Only in Production: this index folder is defined in settings > template > dir
    path("", TemplateView.as_view(template_name="index.html"), name="vue-app"),
    # Only under development:
    # reserved space...
    # Only in Production: this index folder is defined in settings > template > dir
    path(
        "<path:path>",
        TemplateView.as_view(template_name="index.html"),
        name="vue-app-paths",
    ),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
