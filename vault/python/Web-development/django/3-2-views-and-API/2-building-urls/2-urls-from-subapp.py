"""

    URLS.PY FOR SUB-APPS
    ('sub-apps' are every folder in the first level of '/apps/' folder. 'apps' folder need to be manually created as well as each sub-app folder)

    The '/apps/sub-app-name/urls.py' file defines all URLs that belong specifically to a sub-app.
        
    This file deeply depends of the 'urls.py' in Django core folder:
        ./1-urls-from-core-folder.py

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
    ABOUT PATH CONVERTERS:
    ./path-converters.txt
"""
