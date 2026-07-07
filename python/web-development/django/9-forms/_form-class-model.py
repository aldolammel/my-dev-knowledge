class ModelNameForm(forms.ModelForm):
    '''Customizing the xxxxxxxxxxxxxxx detail-view in the CMS.'''

    class Meta:
        model = models.ModelName  # Form tied to this model.
        fields = '__all__'
        # or
        fields = [
            'field_1', 
            'field_3', 
            'field_7',
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