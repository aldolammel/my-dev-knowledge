#### Python > Django > API
# Creating a JSON link for visual inspection on the CMS:

---
## Before:
- Assuming you have done the previous steps from this roadmap: [/python/web-development/django/0-new-project/api](/python/web-development/django/0-new-project/api.md)
- What are list-view and detail-view: [/python/web-development/django/4-cms-admin/\_about](/python/web-development/django/4-cms-admin/_about.md)

---
## Link field for a CMS list-view:
Let's use a [custom method field](/python/web-development/django/4-cms-admin/1-customizing/listview-adding-custom-hyperlink-field.md) but adapting its logic to print out the API link.
In `/apps/subapp/admin.py`:
```python
from django.utils.html import format_html
from . import models

@admin.register(...)
class SomethingAdmin(...):
    
    # ...
    list_display = (
        # ...,
        "json_preview",  # Custom method field!

    )
	# ...

    # Custom method fields:
    def json_preview(self, obj):
		"""Custom method field: to show the JSON data of the object."""
		url = ""
		if obj and obj.slug:
			url = f"http://localhost:8000/api/something/{obj.slug}/?format=json"
			return format_html("<a href='{}' target='_blank'>{}</a>", url, "See")
		return "JSON 404"
		
	# Defining method field labels:
    json_preview.short_description = "JSON" # type: ignore[attr-defined]
```
If you need a URL builder: [/python/web-development/django/utils/aldo-url-builder.py](/python/web-development/django/utils/aldo-url-builder.py)

---
## Link field for a CMS detail-view:
Still in `/apps/subapp/admin.py`, and make sure you already created the custom method field, you'll need to [customize fieldsets for existing object (detail-view)](/python/web-development/django/4-cms-admin/method-get_fieldsets.md), but don't forget to include the custom method field in `readonly_fields` list.
```python
@admin.register(...)
class SomethingAdmin(...):
	# ...
	
	readonly_fields = (
		# ...,
		"json_preview",  # Custom method field!  # Crucial, otherwise a FieldError will be raised!
	)
	
	# All fields exclusively for the CMS' EXISTING object detail-view:
	fieldsets = (
	    (
	        ...,
	        {
	            "fields": (
	                # ...,
	                "json_preview",  # Instead of 'slug'!  # Custom method field!  
	            ),
	        },
	    ),
	    # ...
	)
	# ...
	
	def get_fieldsets(self, request, obj=None):
	    """..."""
	    return self.add_fieldsets if not obj else self.fieldsets
```

---
