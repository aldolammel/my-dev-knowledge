#### Python > Django > Forms > Methods
# Model `clean()` method

---

Django's `clean()` form method performs form-wide validation after individual field validation, allowing you to validate relationships between multiple fields. So it does:

- Runs after individual field `clean_<fieldname>()` methods;
- Used for cross-field validation (e.g., "if field A is X, then field B must be Y")
- Must return the cleaned data dictionary;
- Places errors in `self.add_error()` or raise `ValidationError`;
- Accesses cleaned data via `self.cleaned_data`.

The `clean()` method for Forms is NOT the same of [clean() for Models](/python/web-development/django/3-1-models-database/method-clean.md)!

---
## Structure:
E.g. `clean_fieldname(self)`:
```python
def clean_<fieldname>(self):
    """Built-in Form method to validate an individual form field before the main clean method."""
    
    <fieldname> = self.cleaned_data['<fieldname>']
    
    if case_everything_is_right:
        return <fieldname>
    
    # Otherwise, warning message:
    raise forms.ValidationError("warning message here")  # Once it's an individual-field-clean(), NEVER use ValidationError as dict!
```
E.g. `clean(self)`:
```python
def clean(self):
    """Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
    
    # Get already validated field data:
    cleaned_data = super().clean() or {}
    
    # Add cross-field validation logic
    if cleaned_data.get("end_date") < cleaned_data.get("start_date"):
        self.add_error("end_date", "End date must be after start date")
    
    return cleaned_data  # Always return cleaned_data!
```
---
## Common example:
```python

def clean(self):
    """Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
    cleaned_data = super().clean() or {}

    password = cleaned_data.get("password")
    confirm = cleaned_data.get("confirm_password")
    
    if password != confirm:
        self.add_error("confirm_password", "Passwords must match")
    
    return cleaned_data
```

---
## Differences between Model `clean()` and Form `clean()`:
[/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form](/python/web-development/django/6-errors-and-validations/2-clean-differences-between-model-and-form.md)
## Get to know: `_post_clean()` form method:
[/python/web-development/django/9-forms/method-\_post_clean](/python/web-development/django/9-forms/method-_post_clean.md)
## Useful Form `clean()` examples:
[/python/web-development/django/9-forms/validations/clean-form-examples/\_about](/python/web-development/django/9-forms/validations/clean-form-examples/_about.md)



