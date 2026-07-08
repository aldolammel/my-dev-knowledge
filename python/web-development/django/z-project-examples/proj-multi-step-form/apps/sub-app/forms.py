from django import forms
from . import models


class StepOneForm(forms.ModelForm):
    class Meta:
        # Model tied to populate:
        model = models.Movie
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False'. If the field is editable but for the form it should be readonly_fields, no problem, you can called here!
        fields = [
            'name',
            'released_year',
        ]


class StepTwoForm(forms.ModelForm):
    class Meta:
        # Model tied to populate:
        model = models.Movie
        # Bringing specific fields from the model:
        # Django rule: to be called here, the field CANNOT be 'editable=False'. If the field is editable but for the form it should be readonly_fields, no problem, you can called here!
        fields = [
            'director',
            'rating',
        ]


"""
    MORE OPTIONS:
    /python/web-development/django/9-forms/

"""
