

"""
    DJANGO VIEWS > METHODS: GET_QUERYSET()

    The get_queryset() method in Views.py allows the customization of the initial list of database records that will be retrieved and processed. So its key purposes:

    - Dynamic filtering based on URL params, e.g., grab data from the URL, like a category name or a user ID, and filter the records accordingly;
    - User-Specific Content, displaying data that belongs strictly to the currently logged-in user;
    - Contextual, time-sensitive logic, such as showing only events where date >= timezone.now(), or excluding draft posts for regular visitors.

    >> Not exclusive for Views:
        While commonly used in Django Admin for CMS customization, get_queryset is available in:
        - Class-based views.
        - Django Admin (ModelAdmin.get_queryset()).
        - Model-classes.

    >> What is QuerySet:
        /python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset

    >> Its use in models:
        /python/web-development/django/3-1-models-database/4-querysets/method-get_queryset
    
    >> Its usa in CMS:
        /python/web-development/django/4-cms-admin/method-get_queryset.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# views.py

class JustAnExampleView(...):
    ...

    def get_queryset(self):
        qs = super().get_queryset()
        # Your logic!
        return qs.filter(<logic-result>)

# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# views.py

from django.views.generic import ListView
from .models import Project

class UserProjectListView(ListView):
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        """Built-in method to customize the initial db records list retrieved and processed."""
        # Get the base queryset
        qs = super().get_queryset()
        # Filter it so users only see their own content
        return qs.filter(owner=self.request.user)