"""

    URLS.PY OF SUB-APPS
    
    >> This file is called 'urls.py' and it belongs to a sub-app created by the developer.
        This file should be created manually in the sub-app folder when needed.
        
    >> This file depends of the its relationship with 'urls.py' in core-folder (another file):
    
        /Python/Web-development/django/3-2-views-and-API/2-building-urls/1-urls-from-core-folder.py


"""

from django.urls import path
from . import views

# NAMESPACE
# By convention, it defines the sub-app namespace:
# It'll be used, for example, when we create routes on templates.
app_name = 'recipes'


# EXAMPLE USING FUNCTION-BASED METHOD
# Defining the routes to be used by this sub-app:
urlpatterns = [
    # http://127.0.0.1:8000/recipes or http://127.0.0.1:8000/recipes/index.html
    path('', views.recipes, name='list_view'),
    # http://127.0.0.1:8000/recipes/1
    path('<int:recipe_id>', views.recipe, name='detail_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build the URL's in templates.
]


# EXAMPLE USING CLASS-BASED METHOD
# Defining the routes to be used by this sub-app:
urlpatterns = [
    # http://127.0.0.1:8000/recipes or http://127.0.0.1:8000/recipes/index.html
    path('', views.RecipesList.as_view(), name='list_view'),
    # http://127.0.0.1:8000/recipes/1
    path('<int:pk>', views.RecipeDetail.as_view(), name='detail_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build the URL's in templates.
]


"""
    THERE IS A GLOBAL URLS.PY
    
    This 'recipes/' as a folder in URL is defined in the
    config-folder (in the project, pretty often this folder has the same name of the project).
    In config-folder, you find a file called 'urls.py' as well. There, you must
    define that 'recipes/' or whatever you want.
    
    /Python/Web-development/django/3-2-views-and-API/2-building-urls/urls-from-config-folder.py

    
    ABOUT PATH CONVERTERS:
    /Python/Web-development/django/3-2-views-and-API/2-building-urls/path-converters.txt

"""
