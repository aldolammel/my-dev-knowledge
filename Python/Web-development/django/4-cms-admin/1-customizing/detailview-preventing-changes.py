
"""
    PREVENTING A FIELD EDITION
    
        >> Prevent CMS users to change username fields through the detail-view:
            /Python/Web-development/django/4-cms-admin/customizing/detailview-preventing-username-changes.py
        
        >> Prevent CMS users to change a specific field through the detail-view:
"""

# FILE: /apps/my_app/admin.py

class ExampleAdmin(admin.ModelAdmin):

    readonly_fields = (
        "slug",
        "updated_at",
        "updated_by",
        # Readonly_fields only accept imported method, never with prefix:
        # Reserved space for imported methods...
    )

    # You can avoid this entire method!
    # def get_readonly_fields(self, request, obj=None):
    #     """Built-in method to extend the 'readonly_fields' power."""
    #     if obj:
    #         # For Editing an existing object:
    #         return self.readonly_fields + ("some_field_added_dynamically_here",)
    #     # For Adding a new object:
    #     return self.readonly_fields