"""
    QUERYSETS FOR ADMIN (CMS): FILTERING
"""

from django.contrib import admin
from .models import BrandCarStore, Vehicle, MedicineType


class BrandCarStoreCMS(admin.ModelAdmin):

    # FILTERING THE CMS SECTION:

    """
        Showing only those entries that the 'status' is 'on'!
        This is just an example but is not recommended to hide something from the CMS!
    
    """

    def get_queryset(self, request):
        return super().get_queryset().exclude(status='off')  # type: ignore

    # CMS FIELD FILTERING (DROPDOWN):

    """
        There's a database with a list of many vehicle from different brands. Each brand-seller
        (user) is able to select vehicles already sold. Of course the brand-seller sells vehicles
        of a specific brand. That said, your form should prevent the Ford seller to pick
        a Fiat vehicle, right?
        
            So, how does filter only the Ford vehicles from a database table with many other brands?
    
            Let's go!
            
    """
   
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''This built-in method allows to override the default formfield for a foreign keys field.'''
        # It filters vehicle field by seller's associated brand:
        if db_field.name in ['sold_vehicle']:  # accept many fields here as array!
            # Get the current object being edited:
            obj_id = request.resolver_match.kwargs.get('object_id')  # type: ignore
            if obj_id:
                # Retrieve the related BrandCarStore instance:
                store = BrandCarStore.objects.get(pk=obj_id)
                # Filter the queryset based on the seller (user) associated brand:
                kwargs['queryset'] = Vehicle.objects.filter(brand=store.seller.brand)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    # SIMPLEST EXAMPLE:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        '''This built-in method allows to override the default formfield for a foreign keys field.'''
        if db_field.name == "medicine_type":
            kwargs["queryset"] = MedicineType.objects.filter(status='on')
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    

    """
                    
        FORMS:
        Don't forget to make the filtering also in forms.py (different way) to make the feature
        usefull throught the front-end as well.
        
            /Python/Web-development/django/9-forms/form-queryset-filtering-dropdown.py
    
    """
