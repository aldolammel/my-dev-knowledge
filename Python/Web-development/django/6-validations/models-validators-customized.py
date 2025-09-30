
"""
    DJANGO > VALIDATIONS: CUSTOM MODEL VALIDATOR

    Be aware what you wanna validate indeed does NOT exist as a built-in validator:
        /Python/Web-development/django/6-validations/validation-1-for-database.txt
    
    There are 2 approaches for custom validators:
        1. Work with validate function that can be called multiple times for other fields;
        2. Or work in something do specific, directly in model methods;

        That said, examples below is using only the approach 1, once the approach 2 is easy to understand.

    Remember:
        Function validators always return 'None' or raise a ValidationError message!
"""


# FILE: /apps/my_app/validators.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.core.exceptions import ValidationError

def validate_something(value):  # this 'validate_' is a convention!
    """Validates xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
    if <SOMETHING_COMPLEX_THAT_IS_NOT_VALID>:
        raise ValidationError(
            "An error message here!",
            # Check the code:
            # /Python/Web-development/django/6-validations/error-identification-codes.txt
            code="xxxxxxxxxx",
        )

def validate_goals(p, s):
    """Validates primary and secondary goal fields logic before to save them on the db."""
    if not p and s:
        raise ValidationError(
            "Select a primary goal at least!",
            code="invalid_choice",
        )
    elif p and s and p == s:
        raise ValidationError(
            "Primary and secondary goals cant be the same!",
            code="overlap",
        )


# FILE: /apps/my_app/models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from .validators import validate_something

class ExampleModel(models.Model):
    # ...existing code...
    
    my_field = models.CharField(
        ...
        validators=[validate_something],
    )

    def clean(self):
        """Built-in method for adding custom validation logic before full_clean() or save()."""
        super().clean()
        validate_something(self.my_field, "element")




"""
    CUSTOM VALIDATOR FOR M2M FIELDS (SPECIAL CASE):
        /Python/Web-development/django/6-validations/models-validators-customized-for-m2m.py


    CLEAN() USAGE DIFFERENCES BETWEEN MODELS.PY AND FORMS.PY:
        /Python/Web-development/django/6-validations/clean-differences-between-model-and-form.txt
"""