from django import forms

#from . import constants as consts
from .models import (
    ExampleModel,
)
#from .validators import validate_xxxxxx

"""
class ModelNameForm(forms.ModelForm):
    '''Customizing the xxxxxxxxxxxxxxx detail-view in the CMS.'''

    class Meta:
        model = xxxxxxxxxxxx  # Form tied to this model.
        fields = "__all__"

    # Extra form fields (Not tied to the model):
    # Reserved space...

    def clean(self):
        '''Built-in Form method used to provide custom validation logic after field-level validation, but before the cleaned data's return.'''
        cleaned_data = super().clean()

        xxxxxxxxxx

        return cleaned_data
"""
