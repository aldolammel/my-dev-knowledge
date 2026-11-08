# from django.conf import settings
# from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
# from django.views.generic.base import RedirectView

# CORE ENDPOINTS DECLARATION:
urlpatterns = [
    path('admin/', admin.site.urls),  # http://localhost:8000/admin/
    # APPLICATION:
    path('subappname/', include('apps.subappname.urls')),
    # OTHERS:
    # Remember to check the /urls_api.py!
    # path("", include("core.urls_api")),
]

# DJANGO > ONLY WHEN DEBUG TRUE:
# Reserved space...

# THIRD-PARTY:
# urlpatterns += [
#     Reserved space...
# ]

# FRONTEND:
# urlpatterns += [
#     Reserved space...
# ]
