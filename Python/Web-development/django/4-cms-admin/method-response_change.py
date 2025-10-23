
"""
    DJANGO CMS > METHODS: RESPONSE_CHANGE()

    The response_change() method determines what happens after a model object is successfully changed in the admin interface. It's primarily/exclusively used for the CMS. So it does:

    - Called after an object is successfully saved in the admin change form.
    - Returns an HttpResponse (usually a redirect).
    - Allows customization of what happens after saving.

    >> xxxx:
        /xxxxx
"""

# Default behavior - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Default implementation redirects to:
# 1. The object's changelist if "_continue" wasn't clicked
# 2. Back to the change form if "_continue" was clicked

# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def response_change(self, request, obj):
    """This built-in method defines what happens after an object's successfully changed."""
    # Add custom logic after save
    if obj.status == 'approved':
        send_approval_email(obj)
    
    # Call parent to preserve default behavior
    return super().response_change(request, obj)