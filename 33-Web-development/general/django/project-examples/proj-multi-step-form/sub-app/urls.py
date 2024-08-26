from django.urls import path
from . import views

# Namespace:
app_name = 'sandbox'


urlpatterns = [
    # http://127.0.0.1:8000/sandbox/movies/
    path('movies/', views.movie_list, name='movie_list'),
    # http://127.0.0.1:8000/sandbox/movie/step-one/
    path('movie/step-one/', views.movie_step_one, name='movie_step_one'),
    # http://127.0.0.1:8000/sandbox/movie/step-one/12
    path('movie/step-one/<int:pk>/', views.movie_step_one, name='movie_step_one'),
    # http://127.0.0.1:8000/sandbox/movie/step-two/12
    path('movie/step-two/<int:pk>/', views.movie_step_two, name='movie_step_two'),
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build the URL's in templates.
]


"""
    MORE OPTIONS:
    /33-Web-development/general/django/3-2-backend-views/2-building-urls/urls-from-subapp.py

"""
