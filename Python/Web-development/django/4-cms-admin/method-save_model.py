
"""
    DJANGO CMS > METHODS: SAVE_MODEL()

    The save_model() method is a model instance saving hook that lets you customize what happens when a model is saved through the Django admin interface. So it does:

    - It's called when saving objects in the Django admin.
    - It receives the model instance, the current request, and a boolean indicating if this is a new object or an update.
    - It allows you to modify the object before saving or perform additional actions.

    >> Keep in mind:
    - Use save_model() for admin-specific logic that needs request context.
    - Use model's save() for business logic that should apply everywhere.
    - Use form's save() for form-specific data processing.

    >> The save_model() for Django Models is the save() method for Models:
        /Python/Web-development/django/3-1-models-database/method-save.py
    
    >> The save_model() for Django Forms (including those tied with CMS) is the save() for Forms:
        /Python/Web-development/django/9-forms/method-save.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # custom save code...
        super().save_model(request, obj, form, change)


# Common examples - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        if not obj.pk:  # New object
            obj.created_by = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # Pre-save logic
        if obj.status == 'completed' and not obj.completed_at:
            obj.completed_at = timezone.now()
        
        # Save the object
        super().save_model(request, obj, form, change)
        
        # Post-save logic
        if change:
            self.log_change(request, obj, "Order updated")