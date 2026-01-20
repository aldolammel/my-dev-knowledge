"""
    DJANGO CMS: EXCLUDING A FIELD IN DETAIL-VIEW (BASIC APPROACH)

    For more options, check:
        ./detailview-field-exclusion.py
    
    The idea here is to "filter" which situation a field must be shown: "Only for new objects; only for editable objects, or in both cases?" To organize that, the basic way to do that is using this approach below:
"""

# File: /apps/my_app/admin.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):

    # This basic way doesn't demand you set those admin class tuples like add_fieldsets, fieldsets, neither readonly_fields and get_fieldsets method declaration.

    def my_method_field(self, obj):
        """A field that's not coming from ExampleModel in models.py!"""
        ...
        return ...

    def get_readonly_fields(self, request, obj=None):
        """Built-in method to extend the 'readonly_fields' power."""
        if obj:
            # For existing object:
            return self.readonly_fields + ("my_method_field",)  # type: ignore[operator]
        # For new object:
        return self.readonly_fields

    # Defining method field labels:
    my_method_field.short_description = "My Method Field"  # type: ignore[attr-defined]



