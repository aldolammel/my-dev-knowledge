# FILE: /my_django_project/apps/pagex/urls.py

from core.constants import (
    NAMESPACE_1,
)

# NAMESPACE
app_name = NAMESPACE_1

# These URLs are handled by Vue Router instead, configured through files:
# 1. /pagex/serializers.py
# 2. /pagex/views.py
# 3. /core/urls.py!
urlpatterns = []
