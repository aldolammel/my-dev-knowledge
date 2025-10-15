
"""
    DJANGO > CMS CUSTOMIZATIONS > BUILT-IN METHODS: GET_QUERYSET()

    >> More about:
        /Python/Web-development/django/3-1-models-database/4-querysets/method-get_queryset.txt

    >> Some alternatives to get_queryset():
        ./detailview-filtering-any-data.py
"""


class ExampleModelAdmin(admin.ModelAdmin):

    # Showing only those entries that the 'status' is 'on' (NOT RECOMMENDED):
    """This is just an example coz is NOT recommended to hide objects from the CMS once you can hide just from a single field!"""
    def get_queryset(self, request):
        return super().get_queryset().exclude(status='off')
