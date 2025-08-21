from django.urls import path
from . import views

# Namespace:
app_name = 'movies'


urlpatterns = [
    # http://127.0.0.1:8000/movies/
    path('', views.MoviesListView.as_view(), name='list_view'),
    # http://127.0.0.1:8000/movies/step-one/
    path('step-one/', views.step_one, name='step_one_view'),
    # http://127.0.0.1:8000/movies/step-one/12
    path('step-one/<int:pk>/', views.step_one, name='step_one_view'),
    # http://127.0.0.1:8000/movies/step-two/12
    path('step-two/<int:pk>/', views.step_two, name='step_two_view'),
    # Crucial: this 'name' argument above is the 'pattern name' you'll use to build the URL's in templates.
]


"""
    MORE OPTIONS:
    /Python/Web-development/django/3-2-backend-views/2-building-urls/urls-from-subapp.py

"""
