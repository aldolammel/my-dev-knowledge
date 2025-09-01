from django.urls import path
from . import views
from core.constants import (
    NAMEAPP_3,
    PATTERN_3_1,
    PATTERN_3_2,
    PATTERN_3_3,
    PATTERN_3_4,
    PATTERN_3_5,
    PATTERN_3_6,
    PATTERN_3_7,
    PATTERN_3_8,
    PATTERN_3_9,
)

# Namespace:
app_name = NAMEAPP_3

urlpatterns = [
    # http://127.0.0.1:8000/ap_name/...
    path("register/", views.register, name=PATTERN_3_1),
    path("login/", views.CustomLoginView.as_view(), name=PATTERN_3_3),
    path("password/", views.CustomPasswordChangeView.as_view(), name=PATTERN_3_4),
    path("password_reset/", views.CustomPasswordResetView.as_view(), name=PATTERN_3_5),
    path(
        "password_reset/done/",
        views.CustomPasswordResetDoneView.as_view(),
        name=PATTERN_3_6,
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.CustomPasswordResetConfirmView.as_view(),
        name=PATTERN_3_7,
    ),
    path(
        "reset/done/", views.CustomPasswordResetCompleteView.as_view(), name=PATTERN_3_8
    ),
    path("logout/", views.custom_logout_view, name=PATTERN_3_9),
    path("<str:username>", views.profile_view, name=PATTERN_3_2),
]
