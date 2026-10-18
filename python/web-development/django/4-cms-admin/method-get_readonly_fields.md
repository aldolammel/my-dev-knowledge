#### Python > Django > CMS > Methods
# `get_readonly_fields()` admin model method

---

The `get_readonly_fields()` method determines which fields should be read-only in forms, typically in the CMS. So its key points are:

- It returns a list/tuple of field names that should be displayed as read-only.
- Fields specified will be visible but cannot be edited.
- Can be dynamic based on conditions (unlike the static `readonly_fields` attribute).

**Not exclusive for CMS. It can be used:**

- Main usage, for Django Admin interface.
- Can be used elsewhere, for example while designed for Admin, the pattern can be adapted for regular forms.
- Or by third-party apps like some admin-like interfaces (like django-import-export) may use similar concepts.

---
## Structure:
```python
# soon...
```

---
## Common example:
```python
class MyModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
	    '''Built-in CMS method that allows you to dynamically specify which fields are read-only ('readonly_fields') based on the request or object.'''
        # Get the class-level readonly_fields:
        current = list(self.readonly_fields)
        # Editing an existing object:
        if obj:
            return current + ["element_type"]
        return current
```

---
