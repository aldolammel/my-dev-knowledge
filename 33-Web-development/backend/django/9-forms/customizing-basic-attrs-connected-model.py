
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

class EventAttackModelForm(forms.ModelForm):
    
    class Meta:
        # Connected model to populate:
        model = EventAttackModel
    # Ordering fields on the form:
        fields = [
            'start_date', 
            'is_brazilian', 
            'start_time',
            'is_ongoing',
            'end_date',
            'end_time',
        ]
        # Simple and static tweaks only for connected model's fields:
        widgets = {
            'start_date': forms.DateInput(
                format='%Y-%m-%d',  # Enforcing the db format explicitly!
                attrs={'class': 'input is-large', 'type': 'date'},
            ),
            'is_brazilian': forms.CheckboxInput(
                attrs={'class': 'is-large', 'id': 'is_brazilian'}
            ),
            'start_time': forms.TimeInput(attrs={'class': 'input is-large', 'type': 'time'}),
            'is_ongoing': forms.CheckboxInput(attrs={'class': 'is-large', 'id': 'is_ongoing'}),
            'end_date': forms.DateInput(
                format='%Y-%m-%d',  # Enforcing the db format explicitly!
                attrs={'class': 'input is-large', 'type': 'date'},
            ),
            'end_time': forms.TimeInput(attrs={'class': 'input is-large', 'type': 'time'}),
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

class EventAttackModelForm(forms.ModelForm):
    
    class Meta:
        ...
        
    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        self.fields['start_date'].widget.attrs.update({'type': 'date'})



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

class EventAttackModelForm(forms.ModelForm):
    
    class Meta:
        ...
            
    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        self.fields['start_date'].widget = forms.DateInput(attrs={'type': 'date'})







'''

        B3) Other example of how powerful is to use __init__:

            E.g.
        
        
        
'''

class EventAttackModelForm(forms.ModelForm):
    
    class Meta:
        ...
            
    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        d_current = timezone.now().date()
        d_limit = (timezone.now() - timedelta(days=180)).date()
        self.fields['start_date'].widget.attrs.update({'max': d_current, 'min': d_limit})
        self.fields['end_date'].widget.attrs.update({'max': d_current, 'min': d_limit})





'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    >> How to customize an extra field (not from connected model):
    
        /33-Web-development/backend/django/9-forms/customizing-basic-attrs-extra-field.py
        
        


    >> If you need (for some weird reason) to customize fully a form without Django main assistence:

        /33-Web-development/backend/django/9-forms/customizing-fully-on-template.txt  (Not recommended!)


'''