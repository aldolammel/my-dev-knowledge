from django.urls import path
from . import views

# NAMESPACE
app_name = 'movies'


# EXAMPLE USING ONLY FUNCTION-BASED METHOD
# Defining the routes to be used by this sub-app:
urlpatterns = [
    # http://127.0.0.1:8000/movies/
    path('', views.movie_list, name='movie_list_view'),
    # http://127.0.0.1:8000/movies/add
    path('add/', views.movie_add, name='movie_add_view'),
    # http://127.0.0.1:8000/movies/1
    path('<int:movie_id>', views.movie_edit, name='movie_edit_view'),
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build the URL's in templates.
]


"""
    MORE OPTIONS:
    /Python/Web-development/django/3-2-backend-views/2-building-urls/urls-from-subapp.py

"""
