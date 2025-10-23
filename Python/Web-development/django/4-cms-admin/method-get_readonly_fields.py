
"""
    DJANGO CMS > METHODS: GET_READONLY_FIELDS()

    The get_readonly_fields() method determines which fields should be read-only in forms, typically in the CMS. So its key points are:

    - t returns a list/tuple of field names that should be displayed as read-only.
    - Fields specified will be visible but cannot be edited.
    - Can be dynamic based on conditions (unlike the static readonly_fields attribute).

    >> Not exclusive for CMS. It can be used:
        - Main usage, for Django Admin interface.
        - Can be used elsewhere, for example while designed for Admin, the pattern can be adapted for regular forms.
        - Or by third-party apps like some admin-like interfaces (like django-import-export) may use similar concepts.

    >> xxxx:
        /xxxxx
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 



# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class MyModelAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return ['created_date', 'created_by']
        return []  # Creating a new object