
"""
    DJANGO CMS > ADMIN MODEL OPTION: READONLY_FIELDS

    The readonly_fields is a ModelAdmin option that xxxxxxxxxxxxx.

"""

# Basic structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...

    readonly_fields = (
        xxxxx
    )


# Customizing the data for the filter - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
xxxxxx