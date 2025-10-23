
"""
    DJANGO CMS > METHODS: CHANGE_VIEW()

    The change_view() method is primarily used in the Django Admin interface to handle the form submission when editing an existing object. So it does:

    - Processes POST requests when modifying an existing model instance in the admin.
    - Handles form validation, saving, and redirects.
    - Displays the edit form for GET requests.
    - Manages admin-specific functionality like permission checks and logging.

    >> If you need a method that handle "add" and "update", use chageform_view():
        ./method-changeform_view.py

    >> The regular Django View equivalent of this is the UpdateView:
        /Python/Web-development/django/3-2-views-and-API/viewtype-UpdateView.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# Admin usage (built-in)
class MyModelAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """This built-in method handles only the existing object's form submissions."""
        # Custom admin edit logic
        return super().change_view(request, object_id, form_url, extra_context)


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class OrderAdmin(admin.ModelAdmin):
    def change_view(self, request, object_id, form_url='', extra_context=None):
        """This built-in method handles only the existing object's form submissions."""
        # Only execute for existing objects, not new ones
        order = Order.objects.get(id=object_id)
        
        # Add custom context for change pages only
        extra_context = extra_context or {}
        extra_context['recent_activities'] = order.get_recent_activities()
        extra_context['can_cancel'] = order.can_be_cancelled()
        
        # Restrict editing based on status
        if order.status == 'completed':
            messages.warning(request, "Completed orders have limited editing capabilities")
            
        return super().change_view(request, object_id, form_url, extra_context)