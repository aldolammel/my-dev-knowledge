
"""
    DJANGO VIEWS > METHODS: GET_FORM()

    The get_form() method returns the form class that will be used in a view or admin interface. So its key purposes:

    - Dynamically select which form class to use based on conditions.
    - Modify form behavior without creating multiple views.
    - Customize form validation or fields programmatically.

    >> Not exclusive for Views:
        While commonly used in Django Admin for CMS customization, get_form is available in:
        - Class-based views (CreateView, UpdateView, FormView).
        - Django Admin (ModelAdmin.get_form()).
        - Generic editing views.

    >> Its usage in CMS:
        /Python/Web-development/django/4-cms-admin/method-get_form.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class MyCreateView(CreateView):
    model = MyModel
    
    def get_form(self, form_class=None):
        """Built-in method to customize the form that's displayed in the interface."""
        form = super().get_form(form_class)
        # Customize form here
        return form