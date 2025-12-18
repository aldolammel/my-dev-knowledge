class ModelNameForm(forms.ModelForm):
    '''Customizing the xxxxxxxxxxxxxxx detail-view in the CMS.'''

    class Meta:
        model = xxxxxxxxxxxx  # Form tied to this model.
        fields = "__all__"

    # Extra form fields (Not tied to the model):
    # Reserved space...

    # def save(self, commit=True):
        # """Built-in Form method persists form data to the db."""
        # More about: /Python/Web-development/django/9-forms/method-save.py
    
    def clean(self):
    '''Form-level validation that runs after individual field validations if available.'''
        cleaned_data = super().clean()  # Get already validated field data!

        xxxxxxxxxx

        return cleaned_data