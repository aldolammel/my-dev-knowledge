
'''
   
FORM: BASIC CUSTOMIZING ATTRIBUTES OF AN EXTRA FIELD (NOT FROM CONNECTED MODEL)


    >> All fields of the form-class that are not from the connected model, I call them 'Extra' fields;
    
    >> All extra fields need to be initiated through the form __init__ method to have the chance
        to be populated by database data if applicable.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    A) Declaring the extra fields similar what you do in models;

        E.g.
        
'''

class MyModelForm(forms.ModelForm):
    
    class Meta:
        # Connected model to populate:
        model = ...
        # Ordering fields on the form:
        fields = [
            ...,
            
        ]
        # Simple and static tweaks only for connected model's fields:
        widgets = {
            ...,
        }
        
    # Extra (non-model) fields:
    text_example = forms.TextField(
        required=False,
        Label='First Name',
        widget=forms.TextInput(attrs={'class': 'input is-large'}),
        help_text="You'll need to call this here too.",
    )
    email_example = forms.EmailField(
        required=True,
        label='E-mail'
        widget=forms.TextInput(attrs={'class': 'input is-large'}),
        help_text="You'll need to call this here too.",
    )
    bool_example = forms.BooleanField(
        required=False,
        label='Notify me by email',
        widget=forms.CheckboxInput(attrs={'class': 'is-large', 'id': 'bool_example'}),
        help_text="You'll need to call this here too.",
    )
    # Dropdown menu more dynamic?
    # .../django/4-cms-admin/1-customizing/detailview-dropdown-menu-pointing-to-files.py
    dropdown_example = forms.ModelChoiceField(
        queryset=Language.objects.filter(status='on'),
        required=False,
        label='Language',
        help_text="You'll need to call this here too.",
    )
    datetime_example = forms.DateTimeField(
        required=False,
        label="Password's last update"
        widget=forms.TextInput(attrs={'class': 'input is-small'}),
    )
    password1 = forms.CharField(
        required=True,
        label=lng.LB_PROFILE_PWD_1,
        widget=forms.PasswordInput(attrs={'class': 'input is-large', 'type': 'password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        required=True,
        label=lng.LB_PROFILE_PWD_2,
        widget=forms.PasswordInput(attrs={'class': 'input is-large', 'type': 'password'}),
        help_text=lng.TX_HELP_PROFILE_PWD2,
    )

        
    def __init__(self, *args, **kwargs):
        '''Built-in method called 'Constructor', designed to initialize the instance.'''
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        # Reserved space...
        
        # Extra fields, pre-populating:
        # Unlike fields from connected model, extra fields must be manually linked!
        self.fields['text_example'].initial = user.text_example  # Only if you want to pre-populate this, like for update the db.
        self.fields['email_example'].initial = user.email_example  # Only if you want to pre-populate this, like for update the db.
        self.fields['bool_example'].initial = user.bool_example  # Only if you want to pre-populate this, like for update the db.
        self.fields['dropdown_example'].initial = user.dropdown_example  # Only if you want to pre-populate this, like for update the db.
        self.fields['datetime_example'].initial = user.datetime_example  # Only if you want to pre-populate this, like for update the db.




'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    >> How to customize fields from a connected model:
    
        /Python/Web-development/django/9-forms/customizing-basic-attrs-connected-model.py
        
        


    >> If you need (for some weird reason) to customize fully a form without Django main assistence:

        /Python/Web-development/django/9-forms/customizing-fully-on-template.txt  (Not recommended!)


'''