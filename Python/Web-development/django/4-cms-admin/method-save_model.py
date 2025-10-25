
"""
    DJANGO CMS > METHODS: SAVE_MODEL()

    xxxxx. So it does:

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
        """xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
        # custom save code...
        super().save_model(request, obj, form, change)


# Common examples - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class ArticleAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
        if not obj.pk:  # New object
            obj.created_by = request.user
        obj.last_modified_by = request.user
        super().save_model(request, obj, form, change)


class OrderAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        """xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
        # Pre-save logic
        if obj.status == 'completed' and not obj.completed_at:
            obj.completed_at = timezone.now()
        
        # Save the object
        super().save_model(request, obj, form, change)
        
        # Post-save logic
        if change:
            self.log_change(request, obj, "Order updated")