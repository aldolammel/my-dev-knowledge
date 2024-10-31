
'''
   
FORM: BASIC CUSTOMIZING ATTRIBUTES OF AN EXTRA FIELD (NOT FROM CONNECTED MODEL)


    >> All fields of the form-class that are not from the connected model, I call them 'Extra' fields;
    
    >> All extra fields need to be initiated through the form __init__ method to have the chance
        to be populated by database data if applicable.


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    A) Declaring the extra fields similar what you do in models;

        E.g.
        
'''

class EventAttackModelForm(forms.ModelForm):
    
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
    email = forms.EmailField(
        required=True,
        label='E-mail'
        widget=forms.TextInput(attrs={'class': 'input is-large'}),
        help_text="You'll need to call this here too.",
        error_messages={
            'blank': 'E-mail is required!',
            'invalid': 'Please, enter a valid e-mail.',
        },
    )
    is_notified_by_email = forms.BooleanField(
        required=False,
        label='Notify me by email',
        widget=forms.CheckboxInput(attrs={'class': 'is-large', 'id': 'is_notified_by_email'}),
        help_text="You'll need to call this here too.",
    )
    language = forms.ModelChoiceField(
        queryset=Language.objects.filter(status='on'),
        required=False,
        label='Language',
        help_text="You'll need to call this here too.",
    )
    last_pwd_update = forms.DateTimeField(
        required=False,
        label="Password's last update"
        widget=forms.TextInput(attrs={'class': 'input is-small'}),
    )

        
    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        # Reserved space...
        
        # Extra fields, pre-populating:
        # Unlike fields from connected model, extra fields must be manually linked!
        self.fields['email'].initial = user.email
        self.fields['is_notified_by_email'].initial = user.is_notified_by_email
        self.fields['language'].initial = user.language
        self.fields['last_pwd_update'].initial = user.last_pwd_update




'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    >> How to customize fields from a connected model:
    
        /33-Web-development/backend/django/9-forms/customizing-basic-attrs-connected-model.py
        
        


    >> If you need (for some weird reason) to customize fully a form without Django main assistence:

        /33-Web-development/backend/django/9-forms/customizing-fully-on-template.txt  (Not recommended!)


'''