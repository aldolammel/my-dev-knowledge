
"""
    DJANGO FORMS > VALIDATIONS > CUSTOM VALIDATORS

    CRUCIAL:
        Validators run at the Python/Django level (forms and models, and CMS if the form is associated with the admin-class), BUT NEVER at the database level. So they help prevent invalid data from being saved, however validators DON'T replace database constraints!
    
    Check the built-in validators list:
        /Python/Web-development/django/6-validations/models-validators-built-in.txt
    
    >> Validators only with functions work better when you got simple validations to build,
        otherwise use validations with classes;
    
    >> All validations (created and build-in) work not only on CMS layer, but also on front-end
        and wherever the save() is used by python.
        
    >> At 'A' example, we're building an 'even validator' for a integer field; 
"""



    # A1) You got this class in your sub-app models.py file:

        class RecordingEvenNumbers(model.Model):
            which_number = model.IntegerField()
            
            def __str__(self):
                return str(self.which_number)



    # A2) Let's create its validator to limit its values to even numbers only.
    #    Create a file in your sub-app folder called, e.g., 'validators.py':

        from django.core.exceptions import ValidationError

        def validate_even(value):
            # if the parameter is NOT an integer:
            if not isinstance(value, int):
                # Show a VALUE error:
                raise ValueError('validate_even must take integer numbers only!')
            # if the parameter is NOT an even number:
            if not value % 2 == 0:
                # Show a VALIDATION error:
                raise ValidationError(f'The number {value} is NOT even!')



    # A3) Back to the models.py file, lets apply the validator, first importing
    #    the function previously created:

        from .validators import validate_even

        class RecordingEvenNumbers(model.Model):
            which_number = model.IntegerField(validators=[validate_even])
            
            def __str__(self):
                return str(self.which_number)


