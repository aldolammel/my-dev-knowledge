
"""
    VIEWS CLASSES > CLASS-BASED: USING REDIRECT INHERIT

    >> Handles redirects. It can redirect to a given URL or dynamically compute the URL based
        on the request!

    >> Perfect when you need to redirect a user from one URL to another, such as after
        form submission or for legacy URL support.
"""


# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from django.views.generic.base import RedirectView


class GoToGoogleView(RedirectView):  # This 'View' in classname is a convention.
    url = 'https://google.com/'


"""
    HOW TO USAGE (EXAMPLE):
        ./view-class-redirect-usage.py

    WHO INHERIT REDIRECT-VIEW CLASS:
        >> No one!
"""
