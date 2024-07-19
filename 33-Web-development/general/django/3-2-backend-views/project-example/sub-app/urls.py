from django.urls import path
from . import views

# By convention, it defines the sub-app namespace:
# It'll be used, for example, when we create routes on templates.
app_name = 'recipes'


# Defining the routes to be used by this sub-app:
urlpatterns = [
    # http://127.0.0.1:8000/recipes or http://127.0.0.1:8000/recipes/index.html
    path('', views.recipes, name='list_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build the URL's in templates.
    # http://127.0.0.1:8000/recipes/1
    path('<int:recipe_id>', views.recipe, name='detail_view'),
    # Using class-based views:
    path('testing/', views.RecipesList.as_view())
]


# IMPORTANT:
# this 'recipes/' as a folder in the URL, it's defined in the
# config_folder (in the project, this folder has the same name of the project).
# In config_folder, you find a file called 'urls.py'. There you can
# define that 'recipes/' (kind of a 'directory' to organize URLs).
