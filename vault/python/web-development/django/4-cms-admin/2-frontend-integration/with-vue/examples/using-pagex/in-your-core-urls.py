# THIS FILE IS YOUR /PROJECT_DJANGO/CORE/URLS.PY:

from django.conf import settings
from django.conf.urls.static import static
# from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
# from django.views.generic.base import RedirectView

# DJANGO BASIC:
urlpatterns = [
    # CMS:
    ...
    # SUB-APPs, APIs:
    path("api/", include("apps.pagex.urls")),  # needs to be before the front-end/Vue fallback!
]

# DJANGO > ONLY WHEN DEBUG TRUE:
# Telling to browsers the media path already protected for security reasons. It must be before front-end stuff!
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# THIRD-PARTY:
# urlpatterns += [
#     path("ckeditor/", include("django_ckeditor_5.urls")),
#     path("summernote/", include("django_summernote.urls")),
# ]

# FRONTEND:
urlpatterns += [
    # This index path's defined in settings > template > dir:
    path("", TemplateView.as_view(template_name="index.html"), name="vue-app"),
    path(
        "<path:path>",
        TemplateView.as_view(template_name="index.html"),
        name="vue-app-paths",
    ),
]