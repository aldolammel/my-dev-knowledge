from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Movie


class MovieForm(forms.ModelForm):
    """
    Example of a Model-Form-class, perfect to build a form that will be connected with an existent
    Model-class. It means: the form will interact with the database from the front-end usage.
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
        
        # Built-in method for form initialization:
        def __init__(self, *args, **kwargs):
            movie = kwargs.pop('movie', None)  # Get it from the View!
            super().__init__(*args, **kwargs)
            
            # Pre-populate fields with database data if available:
            if movie:
                self.fields['movie_name'].initial = movie.movie_name
                self.fields['movie_director'].initial = movie.movie_director
                # and 'included_by' ???????????????????????????????
                
        
        """
        
            HOW DOES UPDATE THE DATABASE FROM A FORM:
            
            In order to update the db with the form data, define in your CBV or FBV which
            fields are responsable for the data of each model(s) attributes:
            
                /33-Web-development/general/django/3-2-backend-views/1-building-views-context/
                
        """
            

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
        
        
        
        
class UserProfileTwoCMS(admin.ModelAdmin):
    '''Defining how the UserProfileTwo Model class (business) will exclusivily be shown on the CMS.'''

    list_display = (
        'user',
        'country',  # Imported field from User Model Class!
        'last_login',  # Imported field from User Model Class!
    )
    readonly_fields = (
        'user',
        'first_name',  # Imported field from User Model Class!
        'last_name',  # Imported field from User Model Class!
        'email',  # Imported field from User Model Class!
        'date_joined',  # Imported field from User Model Class!
        'last_login',  # Imported field from User Model Class!
    )
    # exclude = ('', '',)
    list_filter = (
        'user__sex',  # Imported fields as filter: need to call the original class 'user__'!
        'goal_primary',
        'goal_secondary',
    )
    search_fields = [
        'user',
        'user__first_name',  # Imported fields as search: need to call the original class 'user__'!
        'user__last_name',  # Imported fields as search: need to call the original class 'user__'!
    ]

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email

    def sex(self, obj):
        return obj.user.sex

    def date_joined(self, obj):
        return obj.user.date_joined

    def last_login(self, obj):
        return obj.user.last_login

    