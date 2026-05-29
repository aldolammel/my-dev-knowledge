
"""
    DJANGO CMS > METHODS: FORMFIELD_FOR_FOREIGNKEY()

    The formfield_for_foreignkey() method lets you customize the form field used for ForeignKey relationships in Django admin. So it does:

    - Override the default form field for ForeignKey fields.
    - Modify queryset, label, or other field properties.
    - Apply custom filtering or ordering to dropdown options.

    >> In case of a traditional queryset usage:
        ./method-get_queryset.py

    >> Some stuff you could set in here, actually you can use get_form() method too:
        ./method-get_form.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def formfield_for_foreignkey(self, db_field, request, **kwargs):
    """Built-in method that allows to override the default formfield for a foreignkeys field."""
    # Logic here
    return super().formfield_for_foreignkey(db_field, request, **kwargs)


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ArticleAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Built-in method that allows to override the default formfield for a foreignkeys field."""
        if db_field.name == "author":
            # Only show active authors
            kwargs["queryset"] = Author.objects.filter(is_active=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# EXAMPLE 2
class ExampleModelAdmin(admin.ModelAdmin):
    # You're the admin of a blog, and wanna publish a new post behalf someone else:
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        """Built-in method that allows to override the default formfield for a foreignkeys field."""
        if db_field.name == "author":
            kwargs["queryset"] = models.NewsPost.objects.filter(is_working_here_yet=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


# EXAMPLE 3
class ExampleModelAdmin(admin.ModelAdmin):
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