
"""
    DJANGO CMS > METHODS: FORMFIELD_FOR_FOREIGNKEY()

    The formfield_for_foreignkey() method lets you customize the form field used for ForeignKey relationships in Django admin. So it does:

    - Override the default form field for ForeignKey fields.
    - Modify queryset, label, or other field properties.
    - Apply custom filtering or ordering to dropdown options.

    >> xxxx:
        /xxxxx
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