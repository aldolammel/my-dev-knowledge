"""

    FORMS: DYNAMIC DROPDOWN

    FILE: /apps/my_app/forms.py

    How to load filenames as choices:
        .../django/4-cms-admin/1-customizing/detailview-dropdown-menu-pointing-to-files.py
    
"""

from django import forms
from .models import Movie, Language


class MovieForm(forms.ModelForm):
    
    # Built-in meta class:
    class Meta:
        
        # Connecting it (form-class) with the model-class must populate:
        model = Movie

        # Original fields from the associated model. Here you define the field's ordering:
        fields = [
            ...
        ]

    # Extra form fields that will be used to receive data from the template/front-end:

    # example: static dropdown collected from a model (Movie):
    rating = forms.ChoiceField(
        choices=Movie._meta.get_field('rating').choices,
        required=True,
        label='Rating',
    )
    
    # example: dynamic dropdown collected from a model (Language):
    language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=False,
        label='Movie Language',
    )
    
    ...

    # Customizing the form initialization built-in method: 
    def __init__(self, *args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        movie = kwargs.pop('movie', None)  # Get the current movie (from view)!
        super().__init__(*args, **kwargs)
        
        # Pre-populate the form fields with the user data:
        if movie:
            self.fields['ranting'].initial = movie.ranting
            self.fields['language'].initial = movie.language
            ...
