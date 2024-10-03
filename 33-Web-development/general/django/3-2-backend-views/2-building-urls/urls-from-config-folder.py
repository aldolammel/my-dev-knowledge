"""

    URLS.PY FOR CONFIG-FOLDER
    (Config-folder is the folder where you find settings.py file)
    
    >> This file is called 'urls.py' and it belongs to config-folder.
        This file is autocreated when the Django Project is created.
        
    >> This file is the base of all urls.py files probably created into
        each sub-app folder.
        
        /33-Web-development/general/django/3-2-backend-views/2-building-urls/urls-from-subapp.py


"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # DJANGO URLS:
    path('admin/', admin.site.urls),  # http://127.0.0.1:8000/admin/
    # THIRD-PARTY URLS:
    # Reserved space...
    # PRODUCT URLS:
    path('', include('general.urls')),  # sub-app called 'general' example, http://127.0.0.1:8000/
    path('recipes/', include('recipes.urls')),  # http://127.0.0.1:8000/recipes/
    path('url_structure_folder/', include('sub_app_name.urls')),  # Structure example...
]
