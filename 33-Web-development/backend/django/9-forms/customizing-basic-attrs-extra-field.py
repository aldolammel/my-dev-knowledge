
'''
   
FORM: BASIC CUSTOMIZING ATTRIBUTES OF AN EXTRA FIELD (NOT FROM CONNECTED MODEL)


    >> xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:



- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    A) xxxxxxxxxxxxxxxxxxxxx;
        
        Purpose: 
            xxxxxxxxxxxxxxxxxxxxxxx.
        
        Usage: 
            xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.

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
        
    # Extra fields:
    <HEREEEEEEEEEEEEEEEEEEEEEE>
    <HEREEEEEEEEEEEEEEEEEEEEEE>
    <HEREEEEEEEEEEEEEEEEEEEEEE>
    <HEREEEEEEEEEEEEEEEEEEEEEE>
    <HEREEEEEEEEEEEEEEEEEEEEEE>
    <HEREEEEEEEEEEEEEEEEEEEEEE>


'''         
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



    B) XXXXXXXXXXXXXXXX;

        Purpose: 
            XXXXXXXXXXXXXXXXXXXXX

        Usage: 
            XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX



            
'''

class EventAttackModelForm(forms.ModelForm):
    
    class Meta:
        ...
        
    def __init__(self, *args, **kwargs):
        '''Built-in method that's called when the form is initializated.'''
        super().__init__(*args, **kwargs)

        # More complex or dynamic tweaks for connected model's fields:
        # Reserved space...
        
        # Extra fields, pre-populating:
        # Unlike fields from connected model, extra fields must be manually linked!
        <HEREEEEEEEEEEEEEEEEEEEEEE>
        <HEREEEEEEEEEEEEEEEEEEEEEE>
        <HEREEEEEEEEEEEEEEEEEEEEEE>
        <HEREEEEEEEEEEEEEEEEEEEEEE>
        <HEREEEEEEEEEEEEEEEEEEEEEE>
        <HEREEEEEEEEEEEEEEEEEEEEEE>




'''
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


    >> How to customize fields from a connected model:
    
        /33-Web-development/backend/django/9-forms/customizing-basic-attrs-connected-model.py
        
        


    >> If you need (for some weird reason) to customize fully a form without Django main assistence:

        /33-Web-development/backend/django/9-forms/customizing-fully-on-template.txt  (Not recommended!)


'''