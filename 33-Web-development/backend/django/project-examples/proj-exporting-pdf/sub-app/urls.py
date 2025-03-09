from django.urls import path
from . import views

# Namespace:
app_name = "event_attacks"

urlpatterns = [
    # http://127.0.0.1:8000/attacks/attack_list_pdf
    path('attack_list_pdf', views.attack_list_pdf, name='attack_list_pdf'),
]