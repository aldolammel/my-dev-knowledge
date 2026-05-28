from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/', views.movie_detail, name='add_movie'),
    path('movie/<int:movie_id>/', views.movie_detail, name='edit_movie'),
    path('movie/<int:movie_id>/delete/', views.movie_delete, name='delete_movie'),
]
