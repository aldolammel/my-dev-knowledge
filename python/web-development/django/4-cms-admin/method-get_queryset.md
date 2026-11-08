#### Python > Django > CMS > Methods
# `get_queryset()` admin method

---

More about: [/python/web-development/django/3-1-models-database/4-querysets/\_what-is-queryset](/python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md)

Some alternatives to `get_queryset()`: [/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data](/python/web-development/django/4-cms-admin/1-customizing/detailview-filtering-any-data.md)

---
## Structure:
admin.py:
```python
xxxxxxxxxxxxxxxxxx
```

---
## Common example:
admin.py:
```python
class ExampleModelAdmin(admin.ModelAdmin):
	# ...
	
    def get_queryset(self, request):
        """Built-in method to customize the initial db records list retrieved and processed."""
        # Showing only those entries that the 'status' is 'on' (NOT RECOMMENDED FOR ALL SITUATIONS):
        # (This is just an example cuz it's NOT recommended to hide objs from the CMS once you can hide esiear just from a single field!)
        return super().get_queryset().exclude(status='off')
```

---


