#### Python > Django > Forms > Methods
# `_post_clean()` form method

---

**Before:**
- First, you must understand the `clean()` usage: [/python/web-development/django/9-forms/method-clean](/python/web-development/django/9-forms/method-clean.md)

---

Unlike form-level `clean()`, `_post_clean()` runs after the model instance has been constructed (`self.instance`), allowing you to validate state directly against the model object before it is saved.

---
## Structure:
```python
def _post_clean(self):
	'''Built-in Form method that performs additional model-level cleaning and validation after the form's standard fields and form-wide clean methods have executed.'''
	
	# Get already validated field data:
	super()._post_clean()
	
	if <condition>:
		self.add_error(None, "warning message here.")
		
	# Unline the form clean(), you don't return cleaned_data or anything else!
```

---
## Common example:
```python
def _post_clean(self):
	'''Built-in Form method that performs additional model-level cleaning and validation after the form's standard fields and form-wide clean methods have executed.'''
	super()._post_clean()
	# Check the model instance after standard model validation runs
	if self.instance.status == 'published' and not self.instance.author:
		self.add_error(None, "Published articles must have an author.")
```

---
## Same method but for Model Class:
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx