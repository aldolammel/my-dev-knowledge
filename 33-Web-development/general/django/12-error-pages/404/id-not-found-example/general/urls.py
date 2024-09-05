from django.urls import path
from . import views

# Namespace:
app_name = 'general'

urlpatterns = [
    # http://127.0.0.1:8000/404
    path('404', views.error_404, name='404_view'),
]
