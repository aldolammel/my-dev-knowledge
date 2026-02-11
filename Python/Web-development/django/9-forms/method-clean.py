

"""
    DJANGO FORMS > METHODS: CLEAN()

    Django's clean() form method performs form-wide validation after individual field validation, allowing you to validate relationships between multiple fields. So it does:

    - Runs after individual field clean_<fieldname>() methods;
    - Used for cross-field validation (e.g., "if field A is X, then field B must be Y")
    - Must return the cleaned data dictionary;
    - Place errors in self.add_error() or raise ValidationError;
    - Access cleaned data via self.cleaned_data.

    >> The clean() method for Forms is not the same of clean() for Models:
        /Python/Web-development/django/3-1-models-database/method-clean.py

    >> Model clean() VS Form clean():
        /Python/Web-development/django/6-validations/clean-differences-between-model-and-form.txt

"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
def clean_fieldnamehere(self):
    """Field-level form validation."""
    <fieldname> = self.cleaned_data['<fieldname>']
    if some_condition:
        self.add_error('<fieldname>', '<error or warning message>')
    return <fieldname>

def clean(self):
    """Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
    cleaned_data = super().clean()  # Get already validated field data!
    
    # Add cross-field validation logic
    if cleaned_data.get("end_date") < cleaned_data.get("start_date"):
        self.add_error("end_date", "End date must be after start date")
    
    return cleaned_data  # Always return cleaned_data


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def clean(self):
    """Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
    cleaned_data = super().clean()
    password = cleaned_data.get("password")
    confirm = cleaned_data.get("confirm_password")
    
    if password != confirm:
        self.add_error("confirm_password", "Passwords must match")
    
    return cleaned_data