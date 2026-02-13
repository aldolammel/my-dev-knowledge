
"""
    QUERYSETS FOR FORMS: FILTERING A DROPDOWN

    >> There's a database with a list of many vehicle from different brands. Each brand-seller
        (user) is able to select vehicles already sold. Of course the brand-seller sells vehicles
        of a specific brand. That said, your form should prevent the Ford seller to pick
        a Fiat vehicle, right?
        
            So, how does filter only the Ford vehicles from a database table with many other brands?
    
            Let's go!

    >> What are QuerySets?
        /Python/Web-development/django/3-1-models-database/4-querysets/_what-is-queryset.txt
    
"""
from django import forms 
from .models import BrandCarStore, Vehicle

class BrandCarStoreForm(forms.ModelForm):
    
    class Meta:
        # Connected model to populate:
        model = BrandCarStore
        # Ordering fields on the form:
        # fields = []
    
    # Extra fields:
    # Reserved space...
    
    def __init__(self, **args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        seller = kwargs.pop('seller', None)  # 'seller' here is the authenticated User!
        super().__init__(*args, **kwargs)
        
        if seller and seller.brand:
            
            # Connected fields (from connected model), customizations:
            self.fields['sold_vehicle'].queryset = Vehicle.objects.filter(brand=seller.brand)  # type: ignore
            
            # Extra fields, pre-populating:
            # Unlike fields from connected model, extra fields must be manually linked!
            # Reserved space...
            
            
        """
            VIEWS.PY:
            Make sure your View FBV or CBV has in its Context the 'form' with 'seller' data!
            
            CMS:
            Don't forget to make the filtering also in admin.py (different way) to make the feature
            usefull throught the admin area.
            
                /Python/Web-development/django/4-cms-admin/customizing/detailview-filtering-any-data.py

        """