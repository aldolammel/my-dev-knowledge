from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Movie


class MovieForm(forms.ModelForm):
    """
    Example of a Model-Form-class, perfect to build a form that will be connected with a Model-class,
    it means: the form will interact with the database from the front-end.
    """
    
    # Django built-in Meta-class:
    class Meta:
        # Connecting this form-class (MovieForm) to a model-class (Movie), allowing the form
        # to bring automatically model fields/attributes:
        model = Movie
        # Ordering fields on the form, doesn't matter if they're from connected model or extra ones:
        fields = [
            'movie_name',  # coming from connected model (movie)!
            'movie_director',  # coming from connected model!
            'included_by',
        ]
        
        # Extra form fields the connected model doesn't have:
        included_by = forms.CharField(...)
        
        def __init__(self, *args, **kwargs):
            movie = kwargs.pop('movie', None)  # Get it from the View!
            super().__init__(*args, **kwargs)
            # Pre-populate fields with database data if available:
            if movie:
                self.fields['movie_name'].initial = movie.movie_name
                self.fields['movie_director'].initial = movie.movie_director
                # and 'included_by' ???????????????????????????????
            

class CustomUserCreationForm(UserCreationForm):
    """
    Example of a Form-class that inherit its features from a model-form class (UserCreationForm).
    and, at same time, it's connected with a specific model (User).
    """

    class Meta:
        # Connecting it (form-class) with the model-class must populate:
        model = User
        # Specify the fields to include in the form, in the order you want:
        fields = [
            'profile_type',
            'sex',
            'username',
            'email',
            'password1',
            'password2',
        ]
        
        
        EXEMPLO INACABADO!!!!!!!!!!!!!!!!!