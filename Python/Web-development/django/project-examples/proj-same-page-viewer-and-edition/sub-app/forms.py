from django import forms
from .models import Movie


class MovieForm(forms.ModelForm):

    class Meta:
        # Connecting the form with the model/table it will populate:
        model = Movie
        # Bring all class attributes/database columns that will be worked by form:
        fields = '__all__'


"""
    MORE OPTIONS:
    /33-Web-development/backend/python/django/9-forms/

"""
