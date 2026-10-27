#### Python > Django > CMS > Methods
# `get_inline_instances()` admin model method

---
    
The built-in `get_inline_instances()` admin method returns the inline model admin instances to be displayed on another model's admin page. 

You can override it in your custom `ModelAdmin` class.

---
## Structure:
```python
# in admin.py:

# This is the admin class that is defined as a Inline one, bringing all data that should be shown as inline somewhere:
class SomethingInline(admin.StackedInline):
	# ...

class SomethingAdmin(...):

	# Defining what admin class will loaded as a Inline data in this current class:
	inlines = [SomethingInline]
	# ...

	def get_inline_instances(self, request, obj=None):
		"""Built-in admin method that returns the inline model admin instances to be displayed on another model's admin page."""
		
		# Logic here, returning a list or:
		return super().get_inline_instances(request, obj)

```

---
## Common example:
```python
	def get_inline_instances(self, request, obj=None):
		"""Built-in admin method that returns the inline model admin instances to be displayed on another model's admin page."""
		# Imagine you don't wanna the inline field just during the adding detail-view, so just return an empty list:
		if obj is None:
			return []
		return super().get_inline_instances(request, obj)
```

---
## How to use an inline class:
[/python/web-development/django/4-cms-admin/1-customizing/detailview-inline-data-from-another-model](/python/web-development/django/4-cms-admin/1-customizing/detailview-inline-data-from-another-model.md)

---

