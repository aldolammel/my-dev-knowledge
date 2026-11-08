#### Python > Django > CMS > Customizing
# In list-view: adding a new hyperlink-field

---

In `admin.py`:
```python
from django.utils.html import format_html
from . import models

@admin.register(models.MyModelClass)
class MyModelClassAdmin(admin.ModelAdmin):
    
    list_display = (
        'name',
        'page_link',  # Replacing the original Model Class attribute called 'url'!
        'is_new_tab',
    )
    search_fields = [
        "name",
        # "url",
    ]

    # Create a hyperlink to the associated URL to be used on the list-view:
    def page_link(self, obj):
        """To show the URL with link on list-view:"""
        if obj and obj.url:
            return format_html("<a href='{}' target='_blank'>{}</a>", obj.url, obj.url)
        return 'ERROR: Ainda não há link para esta página!'
        
    # Defining method field labels:
    page_link.short_description = "Page Link" # type: ignore[attr-defined]
```

---
## List-view: adding a new field:
[/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-field](/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-field.md)
## List-view: adding a JSON link preview as field:
[python/web-development/django/3-2-views-and-API/admin-json-preview](python/web-development/django/3-2-views-and-API/admin-json-preview.md)


