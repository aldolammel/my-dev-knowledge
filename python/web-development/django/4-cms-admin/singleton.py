"""
    SINGLETON: CREATION WITH DJANGO (STEP 2/3)

    >> What is it:
        /dev-concepts/singleton.md

    >> This file:
        /django_project/apps/your_app/admin.py

    >> Step 1/3 (models.py):
        /python/web-development/django/3-1-models-database/singleton.py

    >> Step 2/3 (admin.py)
        This file!

    >> Step 3/3 (signals.py & apps.py)
        /python/web-development/django/7-middlewares-and-signals/signals/seeding-singleton.md
"""

# subapp/admin.py:


from .models import PagexSettings


@admin.register(PagexSettings)
class PagexSettingsAdmin(admin.ModelAdmin):
    """Settings interface for Pages sub-app. It's a singleton."""

    ...

    def changelist_view(self, request, extra_context=None):
        """Override the list-view to redirect to the singleton instance (detail-view)."""
        # Get or create the settings object:
        obj = PagexSettings.get_settings()
        # Redirect to the change view of the singleton:
        return self.change_view(request, str(obj.pk), extra_context=extra_context)

    def has_add_permission(self, request):
        """Prevent creating more than one singleton object (through list-view and detail-view)."""
        return not PagexSettings.objects.exists()

    def has_delete_permission(self, request, obj=None):
        """Prevent deleting the singleton object (through list-view and detail-view)."""
        return False

    def get_fieldsets(self, request, obj=None):
        """Built-in method that brings all data from fieldsets of the admin class."""
        # If it's in singleton creation step, escape this method:
        if obj is None:
            return self.add_fieldsets
        # Start with base fieldsets:
        fieldsets = list(self.fieldsets) # Way 1, simples!
        fieldsets = list(super().get_fieldsets(request, obj)) # Way 2, safer!
        # here you can set special fields available in certain conditions...
        # If you don't need this, delete the entire get_fieldsets().
        return fieldsets