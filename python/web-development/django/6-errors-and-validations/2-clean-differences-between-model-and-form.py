
"""
    DJANGO FORMS VALIDATIONS > APP-LEVEL/CMS-LEVEL: HOW TO APPLY CLEAN() METHOD FOR MODELS AND FORMS

        clean() is a built-in method that's used in forms and models for cross-field validations or other complex uses. When exactly the clean() method is executaded is different between models and forms cases:

            MODELS CLEAN() METHOD:

                It's used to provide custom model-level validation logic, and is called by full_clean() before saving the object.

            FORMS CLEAN() METHOD:

                On a form, it provides custom validation logic that runs after field-level validation but before cleaned_data is returned.
                
                If an Admin class to demand any clean(), it's mandatory to create a form class (forms.py) once Django doesn't allow the clean() use directly in admin.py.
                
                Unlike its version for models, clean() for forms accepts clean_<fieldname>() to validade a specific field, individualy.

        BASIC KNOWLEDGE:
            ./1-validation-basic.txt

        IMPORTANT:
            All clean() validations written through 'models.py' will automatically propagate on CMS, not mandatorially demanding to add clean() in forms.py (once it's NOT ALLOWED to set clean() method directly in admin.py files). This logic you can read more:
                ./validation-3-for-CMS-forms.txt
"""


# DIFFERENCES BETWEEN CLEAN() FOR MODELS.PY AND FORMS.PY:

    
# For MODEL classes - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    class ExampleModelOne(model.Model):
        ...

        def save(self, *args, **kwargs):
            """Built-in Model method that's executed when the db entry saving runs."""
            # Runs full validation before saving:
            self.full_clean()
            ...

        def clean(self):
            """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
            
            if self.string_one_field == self.string_two_field:
                raise ValidationError(f'Strings cannot be the same!')

        def clean_<fieldname>(self):
            # Individual validation is NOT allowed for models in this way!
            # There, for individual fields, you must use 'Validators'!


# For FORM classes - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    class ExampleModelForm(forms.ModelForm):
        
        class Meta:
            model = ExampleModelOne
            fields = "__all__"

        def clean(self):
            """Built-in Form method to cross-field custom validations at the form level that runs after individuals' clean. Reminder: any clean isn't allowed directly in admin.py."""
            cleaned_data = super().clean()

            # In main forms' clean() you SHOULDN'T use 'self.':
            s1 = cleaned_data.get('string_one_field')
            s2 = cleaned_data.get('string_two_field')

            if s1 and s2 and s1 == s2:
                raise ValidationError({
                    'string_one_field': "Error message 1",
                    'string_two_field': "Error message 2",
                })
            
            return cleaned_data

        def clean_<fieldname>(self):
            """Built-in Form method to validate an individual form field before the main clean method."""
            
            # For individual clean() you MUST use 'self.':
            age = self.cleaned_data.get('age')

            if age and age < 18:
                raise forms.ValidationError("You must be at least 18 years old")
            
            return age



"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    HOW TO BUILD A VALIDATORS.PY:
        ./models-validators-customized.py

    CLEAN() FOR MODELS:
        .../django/3-1-models-database/method-clean.py

    CLEAN() FOR FORMS:
        .../django/9-forms/method-clean.py
"""
