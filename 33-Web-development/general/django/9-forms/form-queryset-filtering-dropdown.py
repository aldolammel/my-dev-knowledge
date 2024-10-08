
"""
    QUERYSETS FOR FORMS: FILTERING A DROPDOWN

    >> There's a database with a list of many vehicle from different brands. Each brand-seller
        (user) is able to select vehicles already sold. Of course the brand-seller sells vehicles
        of a specific brand. That said, your form should prevent the Ford seller to pick
        a Fiat vehicle, right?
        
            So, how does filter only the Ford vehicles from a database table with many other brands?
    
            Let's go!
    
"""
from django import forms 
from .models import BrandCarStore, Vehicle

class BrandCarStoreForm(forms.ModelForm):
    
    class Meta:
        model = BrandCarStore
    
    def __init__(self, **args, **kwargs):
        seller = kwargs.pop('seller', None)  # 'seller' here is the authenticated User!
        super().__init__(*args, **kwargs)
        
        if seller and seller.brand:
            self.fields['sold_vehicle'].queryset = Vehicle.objects.filter(brand=seller.brand)  # type: ignore
            
            
        """
            VIEWS.PY:
            Make sure your View FBV or CBV has in its Context the 'form' with 'seller' data!
            
            CMS:
            Don't forget to make the filtering also in admin.py to make the feature usefull
            throught the admin area.
        
        """