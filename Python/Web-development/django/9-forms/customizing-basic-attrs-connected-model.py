'''
   
FORM: BASIC CUSTOMIZING ATTRIBUTES OF CONNECTED MODEL'S FIELD


    >> There are 2 methods to customize attributes from the connected model in a form:



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    A) Via Widgets-Dictionary in the Meta-Class;
        
        Purpose: 
            Best for static or predictable customizations, where you know the exact fields 
            and the styles they should have ahead of time.
        
        Usage: 
            Set CSS classes or attributes on each widget directly within the form’s 
            Meta class.

        E.g.
        
'''


class MyModelForm(forms.ModelForm):

    class Meta:
        # Connected model to populate:
        model = MyModel
        # Ordering fields on the form:
        fields = [
            'text_example',
            'select_example',
            'email_example',
            'password_example',
            'date_example',
            'time_example',
            'bool_example',
        ]
        # Simple and static tweaks only for connected model's fields:
        widgets = {
            'text_example': forms.TextInput(
                attrs={'class': 'input is-large'},
            ),
            'select_example': forms.Select(attrs={}),
            'email_example': forms.EmailInput(
                attrs={'class': 'input is-large', 'type': 'email'},
            ),
            'password_example': forms.PasswordInput(
                attrs={'class': 'input is-large', 'type': 'password'}
            ),
            'date_example': forms.DateInput(
                format='%Y-%m-%d',  # Enforcing the db format explicitly!
                attrs={'class': 'input is-large', 'type': 'date'},
            ),
            'time_example': forms.TimeInput(attrs={'class': 'input is-large', 'type': 'time'}),
            'bool_example': forms.CheckboxInput(attrs={'class': 'is-large', 'id': 'bool_example'}),
        }


'''         
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



    B) Via Widgets in the __init__ Method;

        Purpose: 
            Useful when you need dynamic customizations that may change based on 
            factors like form state, context, or user preferences.

        Usage: 
            Modify attributes by accessing each form field within the __init__ method, 
            where you can use conditional logic for more complex requirements.



        B1) UPDATING an attribute preserving the original:

            Explanation: 
                This approach modifies the existing widget for start_date by adding or 
                updating attributes.

            Use Case: 
                Useful when you only need to change specific attributes without replacing 
                the entire widget. This keeps any other default settings on the widget 
                intact, adding just the new or updated attributes.

            E.g.
            
'''


class MyModelForm(forms.ModelForm):

    class Meta: ...

    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        self.fields['date_example'].widget.attrs.update({'type': 'date'})


'''

        B2) REPLACING the entiry attributes of the original:

            Explanation: 
                This approach fully replaces the widget of the start_date field with a 
                new DateInput instance.

            Use Case: 
                Useful when you want to entirely redefine the widget, regardless of what 
                was there initially, or if you need to set multiple attributes at once.

            E.g.
        
'''


class MyModelForm(forms.ModelForm):

    class Meta: ...

    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        self.fields['date_example'].widget = forms.DateInput(attrs={'type': 'date'})


'''

        B3) Other example of how powerful is to use __init__:

            E.g.
        
        
        
'''


class MyModelForm(forms.ModelForm):

    class Meta: ...

    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        d_current = timezone.now().date()
        d_limit = (timezone.now() - timedelta(days=180)).date()
        self.fields['date_example'].widget.attrs.update({'max': d_current, 'min': d_limit})


'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    >> How to customize an extra field (not from connected model):
    
        /Python/Web-development/django/9-forms/customizing-basic-attrs-extra-field.py
        
        


    >> If you need (for some weird reason) to customize fully a form without Django main assistence:

        /Python/Web-development/django/9-forms/customizing-fully-on-template.txt  (Not recommended!)


'''
