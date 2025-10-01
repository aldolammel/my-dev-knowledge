
"""
    DJANGO FORMS > VALIDATIONS > CUSTOM VALIDATORS

    CRUCIAL:
        Validators run at the Python/Django level (forms and models, and CMS if the form is associated with the admin-class), BUT NEVER at the database level. So they help prevent invalid data from being saved, however validators DON'T replace database constraints!
    
    Check the built-in validators list:
        /Python/Web-development/django/6-validations/models-validators-built-in.txt
    
    To validate something in a model-class or form-class, you got 2 approaches:
        1. Code the validation directly in the model-class/form-class as a method;
        2. Or create a validator to be used multiple times in different fields or even classes;

        That said, all examples below are using the approach 2, once the first is the same but applied directly in the class.

    Remember:
        Validator functions always return none if successful, or raise a ValidationError message!
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

import re  # for this case!
def validate_product_name(value):
    if not re.match(r'^[A-Za-z0-9 ]+$', value):
        raise ValidationError(
            "Product name can only contain letters, numbers, and spaces.",
            code="invalid",
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
        #param=[arg],
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