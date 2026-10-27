#### Python > Django > CMS > Methods
# `get_urls()` admin model method

---

It belongs only to `admin.py` (or an admin configuration module), so the `get_urls()` admin model method defines and returns the list of URL patterns for the admin interface, allowing you to add, modify, or extend custom admin views and routing.

---
## Structure:
```python
# /apps/subapp_name/admin.py:

from django.contrib import admin
from django.urls import path


class MyModelAdmin(admin.ModelAdmin):
	def get_urls(self):
		'''Built-in admin method that allows you to add or customize URL patterns.'''
		urls = super().get_urls()
		custom_urls = [
			path(
				"my-custom-view/",  # it's the custom URL path like ""add/step-1/".
				self.admin_site.admin_view(self.my_admin_view),
				name="my_custom_view",
			),
		]
		# Custom URLs must come first, or "<path:object_id>/" swallows them:
		return custom_urls + urls

	# Custom method fields:
	def my_admin_view(self, request):
		# Custom view logic here
		pass
```

---
## Common example:
```python
# Soon...
```

---


