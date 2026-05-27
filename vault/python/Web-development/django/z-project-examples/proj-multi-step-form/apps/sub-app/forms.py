from django import forms
from .models import Movie


class StepOneForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['name', 'released_year']


class StepTwoForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['director', 'rating']


"""
    MORE OPTIONS:
    /vault/python/Web-development/django/9-forms/

"""
