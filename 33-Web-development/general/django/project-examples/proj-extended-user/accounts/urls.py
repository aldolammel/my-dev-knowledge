from django.urls import path, include
from . import views
from cefalog.constants import PATTERN_3_1

# Namespace:
app_name = 'accounts'

urlpatterns = [
    # http://127.0.0.1:8000/accounts/register/
    path('register/', views.register, name=PATTERN_3_1),
    # http://127.0.0.1:8000/accounts/aldolammel
    path('<str:username>', views.profile_view, name='profile_view'),
    # http://127.0.0.1:8000/accounts
    # I'm saying that all user accounts must be handle by django that automatically includes
    # pattern-names as 'login' and 'logout':
    path('', include('django.contrib.auth.urls')),
]
