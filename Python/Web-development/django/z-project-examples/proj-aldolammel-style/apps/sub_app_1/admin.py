# from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
# from django import forms as f
from django.contrib import admin

#from . import constants as consts
from . import forms, models

"""
@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    '''Customizes the management of xxxxxxxxxxxxxxxxxxxxxx'''
    
    # Custom form:
    # Reserved space...

    # Custom inlines:
    # Reserved space...

    list_display = (
        "xxxxxxx",
    )
    # exclude = ()
    # filter_horizontal = ()
    # list_filter = ()
    # search_fields = []
    # readonly_fields = ()
    # All fields exclusively for the CMS Adding New object:
    # add_fieldsets = ()
    # All fields exclusively for the CMS Visualizing an object:
    # fieldsets = ()

    # If you have 'created_by' or 'updated_by' you definitely need this method:
    def save_model(self, request, obj, form, change):
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)
"""

# Admin sections that don't need to be customized:
# Reserved space...