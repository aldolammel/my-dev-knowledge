from django import forms

#from . import constants as consts
from .models import (
    ExampleModel,
)
#from .validators import validate_xxxxxx

"""
class ExampleModelForm(forms.ModelForm):
    '''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''
    
    class Meta:
        model = ExampleModel
        fields = "__all__"

    def clean(self):
        '''Built-in Form method used to provide custom validation logic after field-level validation, but before the cleaned data's return.'''
        cleaned_data = super().clean()

        #...

        return cleaned_data
"""
