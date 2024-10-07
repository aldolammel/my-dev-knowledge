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
        # to bring easily model fields/attributes:
        model = Movie
        # Specify the fields to include in the form, in the order you want:
        fields = [
            'movie_name',  # coming from connected model (movie)!
            'movie_director',  # coming from connected model!
            'your_name',
            'your_message',
        ]
        
        # Extra form fields that will be used to receive data from the template/front-end:
        # ...
        


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