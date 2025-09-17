"""
    SINGLETON: CREATION WITH DJANGO (STEP 2/2)

    >> What is it:
        /Programming-Concepts/singleton.txt

    >> This file:
        /django_project/apps/your_app/models.py

    >> Step 1/2 (models.py):
        /Python/Web-development/django/3-1-backend-models-database/singleton.py

    >> Step 2/2 (admin.py)
        This file!
"""

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
        """Brings all data from fieldsets of the admin class."""
        # If it's in singleton creation step, escape this method:
        if obj is None:
            return self.add_fieldsets
        # Start with base fieldsets:
        fieldsets = list(self.fieldsets)
        # here you can set special fields available in certain conditions...
        # If you don't need this, delete the entire get_fieldsets().
        return fieldsets