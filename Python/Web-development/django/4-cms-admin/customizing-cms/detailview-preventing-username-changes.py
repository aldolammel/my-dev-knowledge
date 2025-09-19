
"""
    PREVENTING 'USERNAME' FIELD EDITION
        
        >> Prevent CMS users to change a specific field through the detail-view:
            /Python/Web-development/django/4-cms-admin/customizing-cms/detailview-preventing-changes.py
        
        >> Prevent CMS users to change username fields through the detail-view:
"""


# /accounts/admin.py:


from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


class UserCMS(UserAdmin):
    '''Defining how the User Model class will exclusivily be shown on the CMS.'''

    list_display = (
        'username',
        'email',
        'last_login',
        'is_staff',
        # List_display accept imported fields using prefix and imported method (prefix recommended):
        # Reserved space...
    )
    list_filter = (
        'is_active',
        'is_staff',
        'is_superuser',
        # List_filter only accepts imported fields using prefix:
        # Reserved space...
    )
    search_fields = [
        'username',
        'first_name',
        'last_name',
        'email',
         # Search_fields accept imported fields using prefix and imported method (prefix recommended):
        # Reserved space...
    ]
    readonly_fields = (
        # "username",  # DONT DO THAT! It'd make even the 'CMS Add User' form block the field!
        "date_joined",
        "last_login",
        # Readonly_fields only accept imported method, never with prefix:
        # Reserved space for imported methods...
    )

    def get_readonly_fields(self, request, obj=None):
        """Built-in method to extend the 'readonly_fields' power."""

        if obj:
            # For Editing an existing object:
            return self.readonly_fields + ('username',)
        # For Adding a new object:
        return self.readonly_fields
        



# Registering Django CMS customizations:
admin.site.register(User, UserCMS)
# Registering App CMS features:
# ...