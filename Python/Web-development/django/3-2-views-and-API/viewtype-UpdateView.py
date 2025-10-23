
"""
    DJANGO VIEW TYPES: UPDATEVIEW

    xxxx

    >> xxxxx:
        ./xxxxx

    >> The Admin method equivalent of this is the change_view():
        /Python/Web-development/django/4-cms-admin/method-change_view.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Regular view
from django.views.generic import UpdateView
class MyUpdateView(UpdateView):
    model = MyModel
    template_name = 'my_template.html'
    success_url = '/success/'


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

xxxxx