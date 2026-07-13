class ModelNameForm(forms.ModelForm):
    '''Customizing the xxxxxxxxxxxxxxx detail-view in the CMS.'''

    class Meta:
        # Model tied used to populate it:
        model = models.ModelName
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False', nor custom method. If the field is editable but for the form it should be readonly_fields, no problem, call it!
        fields = '__all__' # Automatically remove fields editable=False!
        # or
        fields = [
            'editable_field_1', 
            'editable_field_2', 
            'editable_field_3_but_also_ReadOnly_for_this_form',
        ]


    # Extra form fields (Not tied to the model):
    # Reserved space...

    # def save(self, commit=True): (RECOMMEND NOT USE IT ONCE YOU GOT THE SAVE() METHOD FROM THE TIED MODEL!)
        # """Built-in Form method persists form data to the db."""
        # More about: /python/web-development/django/9-forms/method-save.py
    
    def clean_<fieldname>(self):
        '''Built-in Form method to validate an individual form field before the main clean method.'''
        something = self.cleaned_data['<fieldname>']
        # Make some individual field validation here!
        return something
    
    def clean(self):
    '''Form-level validation that runs after individual field validations if available.'''
        cleaned_data = super().clean()  # Get already validated field data!

        xxxxxxxxxx

        return cleaned_data