#### Python > Django > CMS > Methods
# `get_fieldsets()` admin method

---

The `get_fieldsets()` method defines how form fields are grouped and organized into sections with optional help text. 

If you wanna take only the field names of a form, try the `get_fields()` method: [/python/web-development/django/4-cms-admin/method-get_fields.py](/python/web-development/django/4-cms-admin/method-get_fields.py)

---
## Structure
```python
readonly_fields = (
	# If you are using add_fieldsets tuple and/or fieldsets tuple, in readonly_fields tuple you MUST include all NON-editable attributes of your model (and eventually your custom method fields), otherwise Django prints out an error!
    "slug",
    "created_at",
    "updated_at",
    "updated_by",
)

# All fields exclusively for the CMS' ADDING new object detail-view:
add_fieldsets = [
    (
        None, {
            'fields': [
                'field1',
                'field2',
            ],
            'description': 'Help text for this section'
        }
    ),
    (
        'Section Title 2', {
            'fields': [
                'field1',
                'field2',
            ],
            'description': 'Help text for this section'
        }
    ),
]

# All fields exclusively for the CMS' EXISTING object detail-view:
fieldsets = [
    (
        None, {
            'fields': [
                'field1',
                'field2',
            ],
            'description': 'Help text for this section'
        }
    ),
    (
        'Section Title 2', {
            'fields': [
                'field1',
                'field2',
            ],
            'description': 'Help text for this section'
        }
    ),
]
```
The `get_fieldsets()` method is mandatory when you're using `add_fieldsets` and/or `fieldsets` benefits:
```python
def get_fieldsets(self, request, obj=None):
    """Built-in method that brings all data from fieldsets of the admin class."""
    # Defines which fieldsets to work from:
    #   'add_fieldsets' are fieldsets of adding new objects;
    #   'fieldsets' are fieldsets of existing objects
    base_fieldsets = self.add_fieldsets if not obj else self.fieldsets
    # Logic here...
    return base_fieldsets
```
Example with even more customizations:
```python
def get_fieldsets(self, request, obj=None):
    """..."""
    # # If it's a page updating, inject page_link_with_help into readonly_fields:
    if obj and "page_link_with_help" not in self.readonly_fields:
        self.readonly_fields += ("page_link_with_help",)  # type: ignore[assignment, misc]
    # Defines which fieldsets to start from:
    base_fieldsets = self.add_fieldsets if not obj else self.fieldsets
    # Convert tuple of tuples into mutable structure:
    fieldsets = []
    pagex_stgs = models.PagexSettings.objects.first()
    is_vue = pagex_stgs and pagex_stgs.front_type == consts.VAL_FRONT_TOOL_VUE
    for title, opts in base_fieldsets:
        fields = list(opts.get("fields", []))
        # Hide vue_component if front_type is NOT Vue:
        if not is_vue and "vue_component" in fields:
            fields.remove("vue_component")
        fieldsets.append((title, {**opts, "fields": fields}))
    return fieldsets
```
Safer way to call all current `fieldsets` (involving inherit/parent classes awareness):
```python
class PagexPageContentInline(admin.StackedInline):
    # ...
    
    def get_fieldsets(self, request, obj=None):
        """..."""

        # This way below means it respects parent classes, mixins, any existing override of get_fieldsets(), and future changes in Django's admin internals:
        fieldsets = list(super().get_fieldsets(request, obj))
        # ...
```