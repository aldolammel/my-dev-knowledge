from django.urls import path
from . import views

# Namespace:
app_name = 'general'

urlpatterns = [
    # http://127.0.0.1:8000/401
    path('401', views.error_401, name='401_view'),
]
