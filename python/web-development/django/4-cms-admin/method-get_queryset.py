

"""
    DJANGO CMS > METHODS: GET_QUERYSET()

    >> More about:
        /python/web-development/django/3-1-models-database/4-querysets/_what-is-queryset.md

    >> Some alternatives to get_queryset():
        ./1-customizing/detailview-filtering-any-data.py
        
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# admin.py




# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# admin.py

class ExampleModelAdmin(admin.ModelAdmin):

    # Showing only those entries that the 'status' is 'on' (NOT RECOMMENDED):
    """This is just an example coz is NOT recommended to hide objects from the CMS once you can hide just from a single field!"""
    def get_queryset(self, request):
        """Built-in method to customize the initial db records list retrieved and processed."""
        return super().get_queryset().exclude(status='off')
