#### Python > Django > Models > Methods
# `clean()` model method

---

It's a method in Django models used for model-level validation. So it does:

- Not automatically called when calling `save()` directly - you need to call `full_clean()` first.
- Called automatically during `full_clean()` and form/model-form validation.
- Validates multiple fields together (unlike field validators which validate single fields).
- If everything alright, `clean()` will return none; otherwise, you should raise a message.
- Raises `ValidationError` if validation fails.
- Used for complex validation logic that depends on multiple fields. 

The `clean()` method for Models is NOT the same of `clean()` for Forms: [/python/web-development/django/9-forms/method-clean](/python/web-development/django/9-forms/method-clean.md)


---
## Structure:
```python
# For parent classes (common):
class ExampleModel(models.Model):
    # ...
    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""

        # Clean validations will run only here through its local attributes!

# For child classes:
class ChildExampleModel(ExampleModel):
    # ...
    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        
        # 1. Allows the parent class to execute full_clean() in this child too:
        super().clean()  # <-- Exactly, not full_clean() here, just clean()!
        
        # 2. And then clean validations for this child runs.


```

---
## Common example:
```python
from django.core.exceptions import ValidationError

class Something(...):
	# ...
	
	def clean(self):
	    """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
	    # Ensure start date is before end date
	    if self.start_date > self.end_date:
	        raise ValidationError("Start date must be before end date")
```

---

