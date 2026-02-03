
"""
    VIEWS CLASSES > CLASS-BASED: USING FORM-VIEW INHERIT

    >> With a form view inherit, you are able to work better with class-based views
        from forms.py file.
"""


# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views.generic.edit import FormView


class MyFormTestView(FormView):  # This 'View' in classname is a convention.
    pass


"""
    HOW TO USAGE (EXAMPLE):
        ./view-class-form-usage.py
"""