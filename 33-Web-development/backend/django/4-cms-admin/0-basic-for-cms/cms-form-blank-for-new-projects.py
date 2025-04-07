from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    
    # Those fields that will be shown on the CMS list-page as columns:
    list_display = (
        'title',
        'slug',
        'img_highlight',
        'content',
        'seo_title',
        'seo_desc',
        'seo_keys',
        'is_published',
        'created_at',
        'updated_at',
    )
    
    # Those fields that must be hidden on the CMS detail-page:
    exclude = (
        #'xxxxxx',
    )
    
    # Those fields that can be data filters on this CMS list page:
    list_filter = (
        'is_published',
    )

    # Those fields that can be read if the search box is used on this CMS page:
    search_fields = [
        'title',
        'content',
    ]
    
    # Those fields that are not editable if you try edit or add the object:
    # Important, if you need to lock a field just, for example, in adding page, you must use the 'get_readonly_fields()' method:
    # /33-Web-development/backend/django/4-cms-admin/customizing-cms/preventing-username-changes.py
    readonly_fields = (
        'created_at',
        'updated_at',
    )
    
    # Defining the Admin layout only:
    fieldsets = (
        (None, {
            # "classes": ("wide",),
            'fields': (
                'title',
                'slug',
            ),
            # 'description': 'xxxxxxxxxxxxxxxxxxxxxxx'
        }),
        ('Content', {
            # "classes": ("wide",),
            'fields': (
                'img_highlight',
                'content',
            ),
            # 'description': 'xxxxxxxxxxxxxxxxxxxxxxx'
        }),
        ('SEO', {
            # "classes": ("wide",),
            'fields': (
                'seo_title',
                'seo_desc',
                'seo_keys',
            ),
            # 'description': 'xxxxxxxxxxxxxxxxxxxxxxx'
        }),
        ('Controlling', {
            # "classes": ("wide",),
            'fields': (
                'is_published',
                'created_at',
                'updated_at',
                #'created_by',
                #'updated_by',
            ),
            # 'description': 'xxxxxxxxxxxxxxxxxxxxxxx'
        })
    )



"""

    IF YOU NEED ADMIN MODEL CLASS EXAMPLES:
    
    /33-Web-development/backend/django/4-cms-admin/0-basic-for-cms/cms-form-examples.py

"""