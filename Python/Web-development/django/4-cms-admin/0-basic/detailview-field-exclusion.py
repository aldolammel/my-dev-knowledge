"""
    DJANGO CMS: EXCLUDING A FIELD IN DETAIL-VIEW

    xxxxxxxxxxxxxxxx
"""

# File: /apps/my_app/models.py 

class ExampleModel(models.Model):
    vue_component = ...
    layout = ...
    is_layouted = ...

# File: /apps/my_app/admin.py 


@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):

    # All fields exclusively for the CMS Adding New object:
    add_fieldsets = (
        ...
        (
            "Conteúdo",
            {
                "fields": (
                    "layout",
                    "vue_component",  # May be removed dynamically if certain conditions are met.
                )
            },
        ),
        ...
    )
    # All fields exclusively for the CMS Visualizing an object:
    fieldsets = (
        ...
        (
            "Conteúdo",
            {
                "fields": (
                    "layout",  # May be removed dynamically if certain conditions are met.
                    "vue_component",  # May be removed dynamically if certain conditions are met.
                )
            },
        ),
        ...
    )

    def get_fields(self, request, obj=None):
        """Built-in method to retrieve a tuple of all field instances associated with a model."""
        fields = list(super().get_fields(request, obj))
        # If Pagex's not using external front-end solution:
        pagex_stgs = PagexSettings.objects.first()
        if pagex_stgs and pagex_stgs.front_type != consts.VAL_FRONT_TOOL_VUE:
            fields.remove("vue_component")
        # If page has layout selected:
        if obj and obj.is_layouted:
            fields.remove("layout")
        return fields