from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('<url_structure_folder>/', include('<sub_app_name>.urls'))
    path('recipes/', include('example-recipes.urls')),
]
