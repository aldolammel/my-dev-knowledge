
"""
    DJANGO > MODEL FORM > CUSTOM VALIDATIONS: USING CLEAN() TO GET DATA AND THEN VALIDATE IT
    
        >> Using clean() method in models.py:
            /Python/Web-development/django/3-1-models-database/model-validation-clean-getting-data.py

        >> Model clean() VS Form clean():
            /Python/Web-development/django/6-validations/clean-differences-between-model-and-form.txt

        >> I'm sure I wanna use clean() method in forms.py:
            KEEP IN THIS FILE!
"""


# HOW TO GET DATA FROM A MODEL TO VALIDATE IT IN FORMS.PY - - - - - - - - - - - - - - - - - - - - -
# /apps/my_app/forms.py:

class ExampleModelForm(forms.ModelForm):

    class Meta:
        model = ExampleModel   # It ties the form to a specific model (models.py).
        fields = "__all__"     # Form will create its form fields based model's attributes (fields).

    def clean(self):
        """Built-in Form method used to provide custom validation logic after field-level validation, but before the cleaned data's return."""
        
        # In clean() method of a form, it's always expected the cleaned_data declaration:
        cleaned_data = super().clean()

        # GETTING DATA USING QUERY SET!
        # Creating a queryset, asking db for this piece of information:
        # /Python/Web-development/django/3-1-models-database/4-querysets/

            # Unlike Model clean() method, the Form clean() demands to return cleaned_data, otherwise, the clean() must return a 'raise ValidationError' message:
            raise ValidationError(...)

        # In clean() method of a form, it's always expected the form returns the cleaned_data:
        return cleaned_data


# HOW TO GET DATA FROM A FIELD FORM AND THEN VALIDATE IT - - - - - - - - - - - - - - - - - - - - - -
# /apps/my_app/forms.py:

class ExampleModelForm(forms.ModelForm):

    class Meta:
        model = ExampleModel
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()

        # Check what user has selected in the receiver_department form field (dropdown menu):
        chosen_department = cleaned_data.get("receiver_department")

        return cleaned_data


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
