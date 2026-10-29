#### Python > Django > Models > Methods
# Model `clean()` method

---

It's a method in Django models used for model-level validation. So it does:

- Not automatically called when calling `save()` directly - you need to call `full_clean()` first.
- Called automatically during `full_clean()` and form/model-form validation.
- Validates multiple fields together (unlike field validators which validate single fields).
- If everything alright, `clean()` will return none; otherwise, you should raise a message.
- Raises `ValidationError` if validation fails.
- Used for complex validation logic that depends on multiple fields. 

The `clean()` method for Models is NOT the same of [clean() for Forms](/python/web-development/django/9-forms/method-clean.md)!

---
## Structure:
```python
# For parent classes (common):
class ExampleModel(models.Model):
    # ...
    def clean(self):
        """Built-in Model method for cross-field, model-level validation. Called by full_clean(), which is NOT called automatically by save(): ModelForm/admin call it, or your code must do so explicitly before save()."""

        # Validations here run through this class's own attributes.

# For child classes:
class ChildExampleModel(ExampleModel):
    # ...
    def clean(self):
        """Built-in Model method for cross-field, model-level validation. Called by full_clean(), which is NOT called automatically by save(): ModelForm/admin call it, or your code must do so explicitly before save()."""

        # 1. Run the parent's clean() validations (not full_clean()!):
        super().clean()

        # 2. Then this child's own validations.
```

---
## Common example:
```python
from django.core.exceptions import ValidationError

class Something(...):
	# ...
	
	def clean(self):
	    """..."""
	    # Ensure start date is before end date
	    if self.start_date > self.end_date:
	        raise ValidationError("Start date must be before end date")
```

---
## Differences between Model `clean()` and Form `clean()`:
[/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form](/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.md)
## Useful Model `clean()` examples:
[/python/web-development/django/3-1-models-database/2-forms-and-validations/clean-model-examples/\_about](/python/web-development/django/3-1-models-database/2-forms-and-validations/clean-model-examples/_about.md)



