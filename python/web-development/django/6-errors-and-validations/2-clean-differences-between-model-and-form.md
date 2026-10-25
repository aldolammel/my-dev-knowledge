#### Python > Django > Validations
# Applying `clean()` method for `models.py` and `forms.py`

---
## Before:
- [Basic validations knowledge](/python/web-development/django/6-errors-and-validations/1-validation-basic.md)

---

`clean()` is a built-in method that's used in forms and models for cross-field validations or other complex uses. When exactly the `clean()` method is executed is different between models and forms cases:
### Models `clean()` method
- It's used to provide custom model-level validation logic, and is called by `full_clean()` before saving the object.
### Forms `clean()` method
- On a form, it provides custom validation logic that runs after field-level validation but before `cleaned_data` is returned.
- If an Admin class to demand any `clean()`, it's mandatory to create a form class (`forms.py`) once Django doesn't allow the `clean()` use directly in `admin.py`.
- Unlike its version for models, `clean()` for forms accepts `clean_<fieldname>()` to validade a specific field, individually.

==Important==
All `clean()` validations written through `models.py` will automatically propagate on CMS, not mandatorily demanding to add `clean()` in `forms.py` (once it's NOT ALLOWED to set `clean()` method directly in `admin.py` files). This logic you can read more: [/python/web-development/django/6-errors-and-validations/validation-3-for-CMS-forms](/python/web-development/django/6-errors-and-validations/validation-3-for-CMS-forms.md)

---
## Differences between `clean()` method from `models.py` and `forms.py`:
### From `models.py`
More about: [/python/web-development/django/3-1-models-database/method-clean](/python/web-development/django/3-1-models-database/method-clean.md)
```python
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

class ExampleModelOne(model.Model):
	# ...

	def save(self, *args, **kwargs):
		'''Built-in Model method that's executed when the db entry saving runs.'''
		# Runs full validation before saving:
		self.full_clean()
		# ...

	def clean(self):
		'''Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance.'''
		
		if self.string_one_field == self.string_two_field:
			
			# Option 1) For messages that are not tied to a specific field. Recommended to use NON_FIELD_ERRORS as key for Django and any DRF serializer get a clear use for this validation.
			raise ValidationError(
				{NON_FIELD_ERRORS: 'The field One and Two cannot be the same.'}
			)
			
			# Option 2) Example to tie the message to a specific field:
			raise ValidationError(
				{'string_one_field': 'The field One cannot be the same of others.'}
			)
			
			# Option 3) Example to tie different messages for every problematic field:
			raise ValidationError(
				{
					'string_one_field': 'The field One cannot be the same of others.',
					'string_two_field': 'The field Two cannot be the same of others.',
				}
			)
			
	# NOT ALLOWED IN MODELS!
	def clean_<fieldname>(self):  # Individual validation is NOT ALLOWED for models in this way!
		# NOT ALLOWED HERE!
		# There, for individual fields, you must use 'Validators'!

```
Making the model validation a bit more dynamic:
```python
raise ValidationError(
	{
		"string_one_field": ValidationError(
			"%(field)s cannot match %(other)s.",
			code="duplicate_value",
			params={"field": "One", "other": "Two"},
		),
	}
)
```
### From `forms.py`
More about: [/python/web-development/django/9-forms/method-clean](/python/web-development/django/9-forms/method-clean.md)
```python
from django.forms import ValidationError            # <---- AVOID to use this because it comes from the django.core.exceptions, kind of an alias!
from django.core.exceptions import ValidationError  # <---- RECOMMENDED, even for forms.py!
from django.core.exceptions import NON_FIELD_ERRORS

class ExampleModelForm(forms.ModelForm):
	
	class Meta:
		# Model tied used to populate it:
		model = ExampleModelOne
		# Bringing specific fields from the model:
		# Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
		fields = "__all__" # Automatically remove fields editable=False!


	def clean(self):
		'''Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py.'''
		cleaned_data = super().clean() or {}

		# In main forms' clean() you SHOULDN'T use 'self.':
		s1 = cleaned_data.get('string_one_field')
		s2 = cleaned_data.get('string_two_field')

		if s1 and s2 and s1 == s2:
			raise ValidationError(
				# EXACTLY THE SAME LOGIC SHOWN IN MODELS.PY, SAME OPTIONS, INCLUDING THE DYNAMIC ONES!
			)
		
		return cleaned_data


	def clean_<fieldname>(self):
		'''Built-in Form method to validate an individual form field before the main clean method.'''
		
		age = self.cleaned_data.get("<fieldname>")
		if age and age < 18:
			raise forms.ValidationError("You must be at least 18 years old")  # Once it's an individual-field-clean(), NEVER use ValidationError as dict!
		return age
```

---
## `validators.py`:
[/python/web-development/django/6-errors-and-validations/models-validators-customized.py](/python/web-development/django/6-errors-and-validations/models-validators-customized.py)
## `clean()` for Models:
[/python/web-development/django/3-1-models-database/method-clean](/python/web-development/django/3-1-models-database/method-clean.md)
## `clean()` for Forms:
[/python/web-development/django/9-forms/method-clean](/python/web-development/django/9-forms/method-clean.md)
## More Python error messages:
[/python/python-knowledge/errors/\_errors-most-common](/python/python-knowledge/errors/_errors-most-common.py)

