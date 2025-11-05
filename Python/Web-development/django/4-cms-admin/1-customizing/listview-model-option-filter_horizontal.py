
"""
    DJANGO CMS > ADMIN MODEL OPTION: FILTER_HORIZONTAL

    The filter_horizontal is a ModelAdmin option that xxxxxxxxxxxxx.

"""

# Basic structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...

    filter_horizontal = (
        "xxxxxxx",
    )


# Customizing the data for the filter - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
xxxxxx