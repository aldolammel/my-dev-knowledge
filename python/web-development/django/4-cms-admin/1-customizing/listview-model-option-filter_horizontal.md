DJANGO CMS > ADMIN MODEL OPTION: FILTER_HORIZONTAL

The `filter_horizontal` is a ModelAdmin option that transform simple [ManyToManyField()](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md) field class presentation to a more user friendly way.

More about: [/python/web-development/django/4-cms-admin/0-basic/cms-m2m-multiple-selection](/python/web-development/django/4-cms-admin/0-basic/cms-m2m-multiple-selection.md)

```python
# Basic structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...
    # Creates a more user-friendly interface for managing many-to-many relationships,
    # displaying two boxes side by side, one with options and another with the selected ones.
    filter_horizontal = (
        'seo_keywords',
    )


# Customizing the data for the filter - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
xxxxxx
```
Image:
![detailview-m2m-horizontal-multi-selection](/python/web-development/django/4-cms-admin/z_imgs/detailview-m2m-horizontal-multi-selection.jpg)