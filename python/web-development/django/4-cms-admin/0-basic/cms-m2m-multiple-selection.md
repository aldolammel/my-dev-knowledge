MANY-TO-MANY USING USER-FRENDLY MULTIPLE SELECTION:

In `admin.py`, inside the Admin Model class:
```python
# Creates a more user-friendly interface for managing many-to-many relationships,
# displaying two boxes side by side, one with options and another with the selected ones.
filter_horizontal = ('seo_keywords',)
```

More about:
- [/python/web-development/django/3-1-models-database/field-select-menu-multiple](/python/web-development/django/3-1-models-database/field-select-menu-multiple.md)
- [/python/web-development/django/4-cms-admin/1-customizing/listview-model-option-filter_horizontal](/python/web-development/django/4-cms-admin/1-customizing/listview-model-option-filter_horizontal.md)

