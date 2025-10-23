
"""
    DJANGO CMS > METHODS: GET_FIELDSETS()

    The get_fieldsets() method defines how form fields are grouped and organized into sections with optional help text. So it does:

    >> If you wanna take only the field names of a form, try the get_fields() method:
        ./method-get_fields.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def get_fieldsets(self, request, obj=None):
    """Built-in method to retrieve a list of tuples, in which each tuple represents a fieldset on the admin form page."""
    # Defines which fieldsets to work from:
    #   'add_fieldsets' are fieldsets of adding new objects;
    #   'fieldsets' are fieldsets of existing objects
    base_fieldsets = self.add_fieldsets if not obj else self.fieldsets
    # Logic here...
    return base_fieldsets

# It can return two lists of tuples where each tuple represents a fieldset:
add_fieldsets = [
    ('Section Title 1', {
        'fields': ['field1'],
        'description': 'Help text for this section'
    }),
    ('Section Title 2', {
        'fields': ['field1'],
        'description': 'Help text for this section'
    }),
]
fieldsets = [
    ('Section Title 1', {
        'fields': ['field1', 'field2'],
        'description': 'Help text for this section'
    }),
    ('Section Title 2', {
        'fields': ['field1', 'field2', 'field3'],
        'description': 'Help text for this section'
    }),
]

# Example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def get_fieldsets(self, request, obj=None):
    """Built-in method to retrieve a list of tuples, in which each tuple represents a fieldset on the admin form page."""
    # # If it's a page updating, inject page_link_with_help into readonly_fields:
    if obj and "page_link_with_help" not in self.readonly_fields:
        self.readonly_fields += ("page_link_with_help",)  # type: ignore[assignment, misc]
    # Defines which fieldsets to start from:
    base_fieldsets = self.add_fieldsets if not obj else self.fieldsets
    # Convert tuple of tuples into mutable structure:
    fieldsets = []
    pagex_stgs = models.PagexSettings.objects.first()
    is_vue = pagex_stgs and pagex_stgs.front_type == consts.VAL_FRONT_TOOL_VUE
    for title, opts in base_fieldsets:
        fields = list(opts.get("fields", []))
        # Hide vue_component if front_type is NOT Vue:
        if not is_vue and "vue_component" in fields:
            fields.remove("vue_component")
        fieldsets.append((title, {**opts, "fields": fields}))
        # If it's a page updating, and page was layouted before, hide content layout field:
        if obj and getattr(obj, "is_layouted", False) and "layout" in fields:
            fields.remove("layout")
    return fieldsets
