#### Python > Django > CMS > Customizing
# In list-view: adding a custom field with counter function

---
In `admin.py`:
```python
from . import models

@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
            
    list_display = (
        'id',
        'name',
        # 'elements',
        'n_elements',  # Custom method field
    )

    def n_elements(self, obj):
        """Custom method field: to count elements."""
        return obj.elements.count()

    # Defining custom method field labels:
    n_elements.short_description = "Nº de elementos"  # type: ignore[attr-defined]
```

---
## List-view: adding a new field:
[/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-field](/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-field.md)

