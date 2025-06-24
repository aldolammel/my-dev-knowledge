from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('<url_structure_folder>/', include('<sub_app_name>.urls'))
    path('movies/', include('movies.urls')),
]


"""
    MORE OPTIONS:
    /33-Web-development/backend/python/django/3-2-backend-views/2-building-urls/urls-from-config-folder.py

"""
