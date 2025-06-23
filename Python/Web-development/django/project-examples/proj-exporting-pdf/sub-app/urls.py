from django.urls import path
from . import views

# Namespace:
app_name = "event_attacks"

urlpatterns = [
    # http://127.0.0.1:8000/attacks/pdf
    path('pdf_<page-name>', views.pdf_<page-name>, name='pdf_<page-name>_view'),
]