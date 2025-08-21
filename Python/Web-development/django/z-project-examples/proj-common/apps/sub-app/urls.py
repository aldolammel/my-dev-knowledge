from django.urls import path
from . import views

# Namespace
app_name = 'recipes'


# EXAMPLE USING FUNCTION-BASED METHOD
# Defining the routes to be used by this sub-app:
urlpatterns = [
    # http://127.0.0.1:8000/recipes or http://127.0.0.1:8000/recipes/index.html
    path('', views.recipes, name='list_view'),
    # http://127.0.0.1:8000/recipes/1
    path('<int:recipe_id>', views.recipe, name='detail_view'),
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build the URL's in templates.
]


"""
    MORE OPTIONS:
    /Python/Web-development/django/3-2-backend-views/2-building-urls/urls-from-subapp.py

"""
