from django.urls import path
from . import views
from core.constants import (
    NAMEAPP_2,
    PATTERN_2_1,
    PATTERN_2_2,
)

# Namespace:
app_name = NAMEAPP_2

urlpatterns = [
    # http://127.0.0.1:8000/app_name/
    path("", views.home_selector_view, name=PATTERN_2_1),
    path("p/", views.home_profile_one_view, name=PATTERN_2_2),
    #path("b/", views.home_profile_two_view, name=PATTERN_2_3),
]
