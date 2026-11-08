#### Python > Django > CMS > Customizing
# In list-view: adding a new field

---

In `admin.py`:
You can create a new column when you create a custom field that exists just here, not coming from some model, for example.
```python
from . import models

@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
            
    list_display = (
        'id',
        'name',
        'new_field_column',  # Custom method field
    )

    def new_field_column(self, obj):
        """Custom method field: to xxxxxxxxxxxxxxxxx."""
        # <your logic here>
        return <string, any...>

    # Defining custom method field labels:
    new_field_column.short_description = "New Field Column Title"  # type: ignore[attr-defined]
```

---
## List-view: adding a custom field with counter function:
[/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-field-with-counter-function](/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-field-with-counter-function.md)
## List-view: adding a new hyperlink-field:
[/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-hyperlink-field](/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-hyperlink-field.md)



