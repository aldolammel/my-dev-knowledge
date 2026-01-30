"""

    URLS.PY FOR CONFIG-FOLDER (CORE)
    ('core' is the folder where you find settings.py file)

    The '/core/urls.py' file is an autocreated project-level URL router, so it's the file that tells Django when a request comes in with this URL, send it to that app/view! Think of it as the traffic controller for the entire project.
        
    All other '/apps/sub_app_name/urls.py' files use this '/core/urls.py' file as router-base.
        
    >> More about those '/apps/sub_app_name/urls.py':
        ./2-urls-from-subapp.py

"""
# from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView

# DJANGO BASIC:
urlpatterns = [
    # CMS:
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    path("admin", RedirectView.as_view(url='/admin/')),
    path("wp-admin/", RedirectView.as_view(url="/admin/")),
    path("wp-admin", RedirectView.as_view(url="/admin/")),
    # SUB-APPs, APIs:
    path('recipes/', include('recipes.urls')),  # http://127.0.0.1:8000/recipes/
    path('url_structure_folder/', include('sub_app_name.urls')),  # Structure example...
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
