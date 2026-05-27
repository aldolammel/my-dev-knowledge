
"""
    DJANGO CMS > ADMIN MODEL OPTION: LIST_DISPLAY

    The list_display is a ModelAdmin option that xxxxxxxxxxxxx.

"""

# Basic structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...

    list_display = (
        "xxxxx",
        "xxxxx",
    )


# Customizing the data for the filter - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
xxxxxx