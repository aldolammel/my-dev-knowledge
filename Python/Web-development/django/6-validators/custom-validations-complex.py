

# CUSTOM VALIDATIONS: COMPLEX WITH CLASSES

'''
    >> Validators with classes work better when you got complex validations to build, otherwise use validations only with functions;
    
    >> All validations (created and build-in) work not only on CMS layer, but also on front-end and wherever the save() is used by python.
        
    >> Important: What is Celery in Django?
    It's a distributed task queue system that can be used with Django to perform asynchronous tasks such as sending emails, processing background jobs, and more. 
        
    >> At 'A' example, we're building a validation checks if the user number is divisible by the system number.
    
'''



    # A1) You got this class in your sub-app models.py file:

        class Divisible(model.Model):
            which_number = model.IntegerField()
            
            def __str__(self):
                return str(self.which_number)



    # A2) Let's create its validator to check if the user number is divisible by the system number.
    #    Create a file in your sub-app folder called, e.g., 'validations.py':

        from django.core.exceptions import ValidationError
        # In order to use classes as validators, let's tell Django some classes here must be celerized (Celery):
        from django.utils.deconstruct import deconstructible


        # This decorate tells django that the class below must be celerized:
        @deconstructible
        class ValidateDiv:
            def __init__(self, user_num):
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
    #    the class previously created:

        from .validators import ValidateDiv

        class Divisible(model.Model):
            system_num = 9
            user_num = model.IntegerField(validators=[ValidateDiv(system_num)])
            
            def __str__(self):
                return str(self.user_num)

