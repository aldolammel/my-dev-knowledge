from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # DJANGO URLS:
    path('admin/', admin.site.urls),
    # THIRD-PARTY URLS:
    # Reserved space...
    # APP URLS:
    path('recipes/', include('example-recipes.urls')),
]
