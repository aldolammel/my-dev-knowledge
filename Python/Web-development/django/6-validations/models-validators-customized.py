
"""
    DJANGO FORMS > VALIDATIONS > CUSTOM VALIDATORS

    CRUCIAL:
        Validators run at the Python/Django level (forms and models, and CMS if the form is associated with the admin-class), BUT NEVER at the database level. So they help prevent invalid data from being saved, however validators DON'T replace database constraints!
    
    Check the built-in validators list:
        /Python/Web-development/django/6-validations/models-validators-built-in.txt
    
    To validate something in a model-class or form-class, you got 3 approaches:

        1. Code the validation directly in the model-class/form-class as a method:
            ./validation-2-for-app-forms.txt
            ./validation-3-for-CMS-forms.txt

        2. Or create a validator to be used multiple times in different fields or even classes;
            THIS SAME FILE!

        3. Or create a sub-version "specialized" of an existent validator:
            ./models-validators-customized-specialized.py

    Remember:
        Validator functions always return none if successful, or raise a ValidationError message!
"""

# FILE: /apps/my_app/validators.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.core.exceptions import ValidationError

def validate_something(value):  # this 'validate_' is a convention for validators!
    """Validates xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx."""
    if <SOMETHING_COMPLEX_THAT_IS_NOT_VALID>:
        raise ValidationError(
            "An error message here!",
            # Check the code:
            # /Python/Web-development/django/6-validations/error-identification-codes.txt
            code="xxxxxxxxxx",
        )

def validate_valid_chars(...):
    # ./validation-custom-only-valid-chars.py

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

from django.utils.translation import gettext_lazy as _  # for this case!
def validate_even(value):
    """Validates for even numbers only."""
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
            code="invalid_choice",
        )


# FILE: /apps/my_app/models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from django.db import models
from .validators import validate_something

class ExampleModel(models.Model):
    ...
    
    my_field = models.CharField(
        ...
        #param=[arg1, arg2, arg3],
        validators=[validate_something],  # Passing the custom via field's 'validators' argument.
    )


# You can use the same custom validator in forms.py too!
# FILE: /apps/my_app/forms.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from django import forms
from .validators import validate_something

class ExampleForm(forms.Form):
    ...
    
    my_field = forms.CharField(
        ...
        validators=[validate_something],
    )


"""
    CUSTOM VALIDATOR FOR M2M FIELDS (SPECIAL CASE):
        /Python/Web-development/django/6-validations/models-validators-customized-for-m2m.py
"""