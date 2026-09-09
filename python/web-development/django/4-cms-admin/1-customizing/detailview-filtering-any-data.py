"""
    QUERYSETS FOR ADMIN (CMS): FILTERING

    What are QuerySets:
        /python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md
"""

# ADMIN.PY
class ExampleModelAdmin(admin.ModelAdmin):


    # FILTERING OBJECTS FROM CMS (NOT RECOMMENDED) - - - - - - - - - - - - - - - - - - - - - - - - -
    # /python/web-development/django/4-cms-admin/method-get_queryset.py


    # FILTERING FROM A FIELD/ATTRIBUTE (DROPDOWN) - - - - - - - - - - - - - - - - - - - - - - - - - 
    # /python/web-development/django/4-cms-admin/method-formfield_for_foreignkey.py
    

 # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    
    
"""
    FORMS.PY:

    Sometimes, the best way to do this is edit the custom form of that admin class OR create one to set this filtering!
    The great stuff in to filtering through the Form Class (forms.py) is the way is reproduced to the app's front-end easily,
    and not just for CMS:

    /python/web-development/django/9-forms/form-queryset-filtering-dropdown.py
"""
