
"""
    DJANGO FORMS VALIDATIONS > APP-LEVEL/CMS-LEVEL: HOW TO APPLY CLEAN() METHOD FOR MODELS AND FORMS

        clean() is a built-in method that's used in forms and models for cross-field validations or other complex uses. When exactly the clean() method is executed is different between models and forms cases:

            MODELS CLEAN() METHOD:

                It's used to provide custom model-level validation logic, and is called by full_clean() before saving the object.

            FORMS CLEAN() METHOD:

                On a form, it provides custom validation logic that runs after field-level validation but before cleaned_data is returned.
                
                If an Admin class to demand any clean(), it's mandatory to create a form class (forms.py) once Django doesn't allow the clean() use directly in admin.py.
                
                Unlike its version for models, clean() for forms accepts clean_<fieldname>() to validade a specific field, individually.

        BASIC KNOWLEDGE:
            ./1-validation-basic.txt

        IMPORTANT:
            All clean() validations written through 'models.py' will automatically propagate on CMS, not mandatorily demanding to add clean() in forms.py (once it's NOT ALLOWED to set clean() method directly in admin.py files). This logic you can read more:
                ./validation-3-for-CMS-forms.txt
"""


# DIFFERENCES BETWEEN CLEAN() FOR MODELS.PY AND FORMS.PY:

    
# For MODEL classes - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# More about: /python/web-development/django/3-1-models-database/method-clean.py

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
                raise ValidationError('Strings cannot be the same!')

        def clean_<fieldname>(self):  # Individual validation is NOT ALLOWED for models in this way!
            # NOT ALLOWED HERE!
            # There, for individual fields, you must use 'Validators'!


# For FORM classes - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# More about: /python/web-development/django/9-forms/method-clean.py

    class ExampleModelForm(forms.ModelForm):
        
        class Meta:
            # Model tied to populate:
            model = ExampleModelOne
            # Bringing specific fields from the model:
            # Django rule: to be called here, the field CANNOT be 'editable=False'. If the field is editable but for the form it should be readonly_fields, no problem, you can called here!
            fields = "__all__" # Automatically remove fields editable=False!


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
            
            age = self.cleaned_data.get("<fieldname>")
            if age and age < 18:
                raise forms.ValidationError("You must be at least 18 years old")  # Once it's an individual-field-clean(), NEVER use ValidationError as dict!
            return age



"""- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    HOW TO BUILD A VALIDATORS.PY:
        ./models-validators-customized.py

    CLEAN() FOR MODELS:
        /python/web-development/django/3-1-models-database/method-clean.py

    CLEAN() FOR FORMS:
        /python/web-development/django/9-forms/method-clean.py
"""
