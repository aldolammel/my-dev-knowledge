"""
    GET AN ADMIN CLASS TEMPLATE:
        1. Concrete Common class.
        2. Concrete Common class with SaveUserMixin inheritance (RECOMMENDED!)
        3. Abstract Mixin class.

"""

# 1. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.contrib import admin
from . import forms, models
# from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
# from django import forms as f
# from . import consts

"""
Admin model class model:
https://...
"""

@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    '''Customizing the management of xxxxxxxxxxxxxxxxx'''

    # Custom form:
    # Reserved space...

    # Custom form template:
    # Automatically searches as: /apps/your_app/templates/admin/your_app/model_name/change_form.html
    # E.g. /python/web-development/django/9-forms/change_form.html
    # For explicit path:
    # change_form_template = "admin/your_app/model_name/change_form.html"

    # Custom inlines:
    # Reserved space...

    # list_display = (
        # "xxxxxxx",
    # )
    # exclude = ()
    # filter_horizontal = ()
    # list_filter = ()
    # search_fields = []
    # readonly_fields = ()
    # All fields exclusively for the CMS' ADDING new object detail-view:
    # add_fieldsets = ()  # If you to use this, it demands get_fieldsets:
        # /python/web-development/django/4-cms-admin/method-get_fieldsets.py
    # All fields exclusively for the CMS' EXISTING object detail-view:
    # fieldsets = ()  # If you to use this, it demands get_fieldsets:
        # /python/web-development/django/4-cms-admin/method-get_fieldsets.py

    # If you have audit fields like 'created_by' or 'updated_by' you need save_model method:
    # def save_model(self, request, obj, form, change):
        '''Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface.'''
        # Sending to models.py the current user in CMS:
        # obj.save(user=request.user)

    # Custom method fields:
    # Reserved space...

    # Defining custom method field labels:
    # Reserved space...


# 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.contrib import admin
from . import forms, models
# from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
# from django import forms as f
# from . import consts

"""
Admin model class model:
https://...
"""

@admin.register(models.ExampleModel)
class ExampleModelAdmin(SaveUserMixin, admin.ModelAdmin):
    '''Customizing the management of xxxxxxxxxxxxxxxxx'''

    # Custom form:
    # Reserved space...

    # Custom form template:
    # Automatically searches as: /apps/your_app/templates/admin/your_app/model_name/change_form.html
    # E.g. /python/web-development/django/9-forms/change_form.html
    # For explicit path:
    # change_form_template = "admin/your_app/model_name/change_form.html"

    # Custom inlines:
    # Reserved space...

    # list_display = (
        # "xxxxxxx",
    # )
    # exclude = ()
    # filter_horizontal = ()
    # list_filter = ()
    # search_fields = []
    readonly_fields = (
        "created_at",
        "created_by",
        "updated_at",
        "updated_by",
    )
    # All fields exclusively for the CMS' ADDING new object detail-view:
    # add_fieldsets = ()  # If you to use this, it demands get_fieldsets:
        # /python/web-development/django/4-cms-admin/method-get_fieldsets.py
    # All fields exclusively for the CMS' EXISTING object detail-view:
    # fieldsets = ()  # If you to use this, it demands get_fieldsets:
        # /python/web-development/django/4-cms-admin/method-get_fieldsets.py

    # If you have audit fields like 'created_by' or 'updated_by' you need save_model method:
    # def save_model(self, request, obj, form, change):
        '''Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface.'''
        # Sending to models.py the current user in CMS:
        # obj.save(user=request.user)

    # Custom method fields:
    # Reserved space...

    # Defining custom method field labels:
    # Reserved space...


# x. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
Admin model class model:
https://...
"""

class SaveUserMixin:
    """Mixin class that automatically passes the current user to the model's save method."""

    def save_model(self, request, obj, form, change):
        """Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface."""
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)

