from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # DJANGO URLS:
    path('admin/', admin.site.urls),

    # APIs:
    # Reserved space...

    # THIRD-PARTY URLS:
    # Reserved space...

    # SUB-APPS:
    path('recipes/', include('example-recipes.urls')),

    # FRONTEND:
    # Reserved space...
]
