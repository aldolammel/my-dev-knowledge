from django.urls import path
from . import views
from core.constants import (
    NAMEAPP_1,
    PATTERN_1_1,
    PATTERN_1_3,
    PATTERN_1_4,
    PATTERN_1_5,
)

# Namespace:
app_name = NAMEAPP_1

urlpatterns = [
    # http://127.0.0.1:8000/
    path("", views.HomeProfileOneView.as_view(), name=PATTERN_1_1),
    # http://127.0.0.1:8000/business/
    #path("business/", views.HomeProfileTwoView.as_view(), name=PATTERN_1_2),
    path("help/", views.HelpView.as_view(), name=PATTERN_1_3),
    path("about/", views.AboutView.as_view(), name=PATTERN_1_5),
    path("privacy-policy/", views.PrivacyPolicyView.as_view(), name=PATTERN_1_4),
]
