
"""
    DJANGO > MODEL > CUSTOM VALIDATIONS: USING CLEAN() TO GET DATA AND THEN VALIDATE IT
    
        >> Using clean() method in forms.py:
            /Python/Web-development/django/9-forms/form-validation-clean-getting-data.py

        >> Model clean() VS Form clean():
            /Python/Web-development/django/6-validations/clean-differences-between-model-and-form.txt
        
        >> I'm sure I wanna use clean() method in models.py:
            KEEP IN THIS FILE!
"""


# HOW TO GET DATA FROM A MODEL TO VALIDATE ITSELF STILL IN MODELS.PY - - - - - - - - - - - - - - - -
# /apps/my_app/models.py:

class ExampleModel(models.Model):

    id = ...
    title = ...

    def clean(self):
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""

        # Once the clean() is applied directly as a method in the model, to call the model (instance) data from db, just use 'self' to refer data from the own instance:
        if self.title:
            ...

            # Unlike Form clean() method, the Model clean() returns nothing if no validation error, otherwise, it expects the 'raise ValidationError' usage:
            raise ValidationError(...)


# HOW TO GET DATA FROM ANOTHER MODEL TO VALIDATE THE CURRENT MODEL STILL IN MODELS.PY - - - - - - - 
# /apps/my_app/models.py:

class MyModelMoreData(models.Model):
    ...


class MyModel(models.Model):

    id = ...

    def clean(self):
        # Only for existent instances, ignoring new instances (because new ones has no id yet):
        if self.pk:
            # Check if there is data from another model:
            is_data_available = MyModelMoreData.object.filter(status='True').exists()
            if not is_data_available:
                raise ValidationError("Feedback error message here...")

        # In this example, you see I'm calling data from this model (MyModel) itself using 'self', and calling data from another model (MyModelMoreData) through a queryset.


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
