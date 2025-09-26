"""
    QUERYSETS FOR ADMIN (CMS): FILTERING

    What are QuerySets:
        /Python/Web-development/django/3-1-backend-models-database/4-querysets/_what-is-queryset.txt
"""


class ExampleModelAdmin(admin.ModelAdmin):


    # FILTERING OBJECTS FROM CMS (NOT RECOMMENDED) - - - - - - - - - - - - - - - - - - - - - - - - -

    """Showing only those entries that the 'status' is 'on'!
    This is just an example coz is NOT recommended to hide objects from the CMS once you can hide just from a single field!"""
    def get_queryset(self, request):
        return super().get_queryset().exclude(status='off')  # type: ignore




    # FILTERING FROM A FIELD/ATTRIBUTE (DROPDOWN) - - - - - - - - - - - - - - - - - - - - - - - - - 


    # Example 1:
    # You're the admin af a blog, and wanna publish a new post behalf someone else:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Built-in method that allows to override the default formfield for a foreignkeys field."""
        if db_field.name == "author":
            kwargs["queryset"] = models.NewsPost.objects.filter(is_working_here_yet=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    # Example 2:
    # You're a car-seller but you sell only Ford vehicles:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Built-in method that allows to override the default formfield for a foreignkeys field."""
        if db_field.name in ["sold_vehicle"]:  # accept many fields here as array!
            # Get the current object being edited:
            obj_id = request.resolver_match.kwargs.get('object_id')  # type: ignore
            if obj_id:
                # Retrieve the related BrandCarStore instance:
                store = BrandCarStore.objects.get(pk=obj_id)
                # Filter the queryset based on the seller (user) associated brand:
                kwargs['queryset'] = Vehicle.objects.filter(brand=store.seller.brand)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    
    

# FORMS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
"""Don't forget to make the filtering also in forms.py (different way) to make the feature usefull throught the front-end as well.
    /Python/Web-development/django/9-forms/form-queryset-filtering-dropdown.py
"""
