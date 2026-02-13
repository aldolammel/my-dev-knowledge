
"""
    DJANGO FORMS > VALIDATIONS > CUSTOM VALIDATORS

    CRUCIAL:
        Validators run at app, forms, and model levels, BUT NEVER at the database level. So they help prevent invalid data from being saved, however validators DON'T replace database constraints!

    IMPORTANT:
        Validator functions always return none if successful, or raise a ValidationError message!
        As well as they are strongly recommended to be used only with model-classes (models.py)!

    Check the built-in validators list:
        ./models-validators-built-in.txt

    How to create a custom validator:
        THIS FILE!

    How to create an existing validator's sub-version (specialized):
        ./models-validators-customized-specialized.py
"""

# FILE: /apps/my_app/validators.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.core.exceptions import ValidationError

def validate_something(value):  # this 'validate_' is a convention for validators!
    """Validates xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx. If alright, it returns None."""
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
    """Validates primary and secondary goal fields logic before to save them on the db. If alright, it returns None."""
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
    """Validates for even numbers only. If alright, it returns None."""
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


# BELOW, DEMANDS REVIEW !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


    # A1) You got this class in your sub-app models.py file:

        class Divisible(model.Model):
            which_number = model.IntegerField()
            
            def __str__(self):
                return str(self.which_number)

    # A2) Let's create its validator to check if the user number is divisible by the system number.
    # Create a file in your sub-app folder called, e.g., 'validations.py':

        from django.core.exceptions import ValidationError
        # In order to use classes as validators, let's tell Django some classes here must be celerized (Celery):
        from django.utils.deconstruct import deconstructible


        # This decorate tells django that the class below must be celerized:
        @deconstructible
        class ValidateDiv:
            def __init__(self, user_num):
                """Dunder method called 'constructor' that runs automatically when a class instance is created."""
                self.user_num = user_num
                
            def __call__(self, system_num):
                # if the parameter 'system_num' is NOT an integer:
                if not isinstance(system_num, int):
                    # Show a VALUE error:
                    return ValueError('ValidateDiv must take integer numbers only!')
                # if the 'system_num' is NOT divisible by the parameter 'user_num':
                if not system_num % self.user_num == 0:
                    # Show a VALIDATION error:
                    raise ValidationError(f'The number {system_num} is NOT divisible by {self.user_num}!')



    # A3) Back to the models.py file, lets apply the validator, first importing
    # the class previously created:

        from .validators import ValidateDiv

        class Divisible(model.Model):
            system_num = 9
            user_num = model.IntegerField(validators=[ValidateDiv(system_num)])
            
            def __str__(self):
                return str(self.user_num)

