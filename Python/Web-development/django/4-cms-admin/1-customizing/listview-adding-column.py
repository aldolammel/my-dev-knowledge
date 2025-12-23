
"""
DJANGO CMS > LIST-VIEW: ADDING A NEW COLUMN

You can create a new column when you create a custom field that exists just here, not coming from some model, for example.
"""

# FILE: /admin.py
from . import models


@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
            
    list_display = (
        'id',
        'name',
        'new_field_column',  # Custom method field
    )

    def new_field_column(self, obj):
            """Custom method field for xxxxxxxxxxxxxxxxx."""
            # <your logic here>
            return <string, any...>

        new_field_column.short_description = "New Field Column Title"  # type: ignore[attr-defined]



"""

HOW TO ADD A COLUMN WITH A COUNTER:
    ./listview-adding-column-counter.py

HOW TO ADD A COLUMN WITH A HYPERLINK:
    ./listview-adding-column-hyperlink.py

"""