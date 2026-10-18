#### Python > Django > CMS > Methods
# `add_view()` admin model method

---

It belongs only to `admin.py`. So the `add_view()` is a built-in method on `ModelAdmin` that handles the view logic for adding a new model instance in the Django admin.

---
## Structure:
```python
def add_view(self, request, form_url="", extra_context=None):
  '''Built-in Django admin method that handles the view logic and form processing for adding a new model instance in the admin interface.'''


```

---
## Common example:
When we use an adding multi-step form on CMS without any app-level core dependency, it's common to use add_view, for example.
```python
from django.contrib import messages
from django.http import HttpResponseRedirect

WIZARD_SESSION_KEY = "step_common_wizard"
WIZARD_STEP_PARAM = "step"

# screen 2:
def add_view(self, request, form_url="", extra_context=None):
	'''Built-in CMS method that handles the view logic and form processing for adding a new model instance in the admin interface.'''
	
	has_data = WIZARD_SESSION_KEY in request.session
	if request.GET.get(WIZARD_STEP_PARAM) != "2" or not has_data:
		if request.GET.get(WIZARD_STEP_PARAM) == "2":
			messages.info(request, "Choose the step basics first.")
		return HttpResponseRedirect(self._start_url())
	return super().add_view(request, form_url, extra_context)
```

---

