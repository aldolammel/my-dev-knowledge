
"""
    DJANGO CMS > ADMIN MODEL OPTION: SEARCH_FIELDS

    The search_fields is a ModelAdmin option that xxxxxxxxxxxxx.

"""

# Basic structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...

    search_fields = [
        "xxxxx",
        "xxxxx",
    ]


# Customizing the data for the filter - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
xxxxxx