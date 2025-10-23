
"""
    DJANGO CMS > METHODS: GET_FIELDS()

    The get_fields() method returns a list of all field names for a model. It's commonly used to programmatically access a model's field definitions. And, no, it's NOT exclusive for the CMS. It's available on any Django model and can be used in views, serializers, forms, management commands, etc.

    CMS vs Regular usage:
    - Admin: Uses it internally to determine which fields to display.
    - Your Code: Can use it anywhere you need to work with model fields dynamically.

    >> If you wanna take the entire fieldsets of a form, try the get_fieldsets() method:
        ./method-get_fieldsets.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def get_fields(self, request, obj=None):
    """Built-in method to retrieve a tuple of all field instances associated with a model."""
    fields = list(super().get_fields(request, obj))
    # logic here!
    return fields


# Flexibility - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

from myapp.models import MyModel

# Get all field names
field_names = [field.name for field in MyModel._meta.get_fields()]
print(field_names)  # ['id', 'title', 'created_at', 'author', ...]

# Useful for:
# - Dynamic form generation.
# - Serializer introspection.
# - Data export/import utilities.
# - Generic views that work with any model.
# - Automated testing.


# Real example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_fields(self, request, obj=None):
    """Built-in method to retrieve a tuple of all field instances associated with a model."""
    fields = list(super().get_fields(request, obj))
    pagex_stgs = models.PagexSettings.objects.first()
    # If Pagex's not using external front-end solution, hide vue_component:
    if (
        # If singleton already exists,
        pagex_stgs
        # and front-end solution is Vue on db,
        and pagex_stgs.front_type != consts.VAL_FRONT_TOOL_VUE
        # and vue_component is in the fields list:
        and "vue_component" in fields
    ):
        fields.remove("vue_component")
    # Only for page updating, hide content layout field if page is already layouted:
    if (
        # If it's a page updating,
        obj
        # and the page is already layouted,
        and getattr(obj, "is_layouted", False)
        # and layout belongs the current fields' list:
        and "layout" in fields
    ):
        fields.remove("layout")
    return fields