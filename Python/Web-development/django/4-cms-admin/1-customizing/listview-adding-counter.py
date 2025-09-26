# FILE: /admin.py

class ExampleModelAdmin(admin.ModelAdmin):
            
    list_display = (
        'id',
        'name',
        # 'elements',
        'n_elements',  # Custom method field
    )

def n_elements(self, obj):
        """Method field for count elements."""
        return obj.elements.count()

    n_elements.short_description = "Nº de elementos"  # type: ignore[attr-defined]