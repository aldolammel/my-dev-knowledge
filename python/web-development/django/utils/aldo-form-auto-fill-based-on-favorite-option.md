#### Python > Django > Utils
# Auto fill form fields based on known use preferences

---
## Context:
You know from User/UserProfile table data what preferences they got, so you can use that to auto-fill form fields if possible.

---
## In `utils.py`:
Creating function to retrieve the user preferences on the database:
```python
def load_user_preference(
	source_table: str,
	self,
	request,
	self_instance_rawattname_id: str,
	form_field_name: str,
	obj_field_name_id: str,
):
	'''Loads a default user preference for a form field if no value is set. For new instances or empty fields, falls back to the user's favorite ID stored on `request.user`. Once selected manually, the favorite is ignored. To call:
	
	self.initial["something"] = utils.load_user_preference(
	"user_table" (or "profile_table")
	self,
	self.request, (or request)
	self.instance.something_id,
	"something",
	"something_favorite_id",
	)'''

	current_id = self.initial.get(form_field_name)
	if self_instance_rawattname_id is None and current_id is None:
		if source_table == "user_table":
			obj = request.user
		elif source_table == "profile_table":
			obj = getattr(request.user, "user_profile", None) # "user_profile" = related_name!
		current_id = getattr(obj, obj_field_name_id, None) if obj else None
		if current_id is not None:
			return current_id
	return current_id
```

---
## In `forms.py`:
The function was developed to be used with forms' `__init__` dunder:
```python
from . import utils

class SomethingForm(...):
	# ...

	def __init__(self, *args, **kwargs):
		'''...'''
		
		# Access the request attached via admin get_form():
		self.request = kwargs.pop("request", getattr(self, "request", None))
		
		super().__init__(*args, **kwargs)
		
		# FAVORITE PLATFORM
		# If applicable, auto-select a user preference:
		self.initial["platform"] = utils.load_user_preference(
			"user_table",
			self,
			self.request,
			self.instance.platform_id,
			"platform",
			"plat_favorite_id",
		)
		
		# FAVORITE LANGUAGE
		# If applicable, auto-select a user preference:
		self.initial["language"] = utils.load_user_preference(
			"profile_table",
			self,
			self.request,
			self.instance.language_id,
			"language",
			"lang_writing_id",
		)
```
Be aware: If you are using a [multi-step adding solution like this one](/python/web-development/django/4-cms-admin/1-customizing/cms-multi-step-adding-using-session.md), likely you should set the code above in the initial form!

---
## In `admin.py`:
In case the admin class tied to the form is not passing the `request` object yet, make the form see the `request.user` through the `get_form()` method.
```python
from . import forms, models

@admin.register(models.Something)
class SomethingAdmin(admin.ModelAdmin):

	form = forms.SomethingForm
	# ...
	
	def get_form(self, request, obj=None, change=False, **kwargs):
		'''Built-in admin method to customize the form that's displayed in the interface.'''
		
		# Sending the 'request' object to the form:
		form = super().get_form(request, obj, change, **kwargs)
		form.request = request  # type: ignore[attr-defined]
		
		return form
```
---


