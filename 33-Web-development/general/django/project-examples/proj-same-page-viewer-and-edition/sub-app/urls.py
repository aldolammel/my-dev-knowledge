from django.urls import path
from . import views

# By convention, it defines the sub-app namespace:
# It'll be used, for example, when we create routes on templates.
app_name = 'movies'


# EXAMPLE USING ONLY FUNCTION-BASED METHOD:
# Defining the routes to be used by this sub-app:
urlpatterns = [
    # http://127.0.0.1:8000/movies/
    path('', views.movie_list, name='movie_list_view'),
    # http://127.0.0.1:8000/movies/add
    path('add/', views.movie_add, name='movie_add_view'),
    # http://127.0.0.1:8000/movies/1
    path('<int:movie_id>', views.movie_edit, name='movie_edit_view'),
    # Crucial: this 'name' above is the 'pattern name' you'll use to build the URL's in templates.
]


# IMPORTANT:
# This 'movies/' as a folder in the URL, it's defined in the
# config_folder (in the project, this folder has the same name of the project).
# In config_folder, you find a file called 'urls.py'. There you can
# define that 'movies/' (kind of a 'directory' to organize URLs).
