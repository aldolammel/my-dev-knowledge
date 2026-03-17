"""
    DJANGO CMS: EXCLUDING A FIELD IN DETAIL-VIEW (DETAILED APPROACH)

    For basic approach:
        ./detailview-field-exclusion-basic.py

    For fieldset approach:
        ./detailview-fieldset-exclusion.py

    The idea here is to "filter" which situation a field must be shown: "Only for new objects; only for editable objects, or in both cases?" To organize that, let's use the 'add_fieldsets' and 'fieldsets' tuples benefits inside the admin class:
"""

# File: /apps/my_app/models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Let's imagine you have this model with these attributes:
class ExampleModel(models.Model):
    site_type = ...
    vue_component = ...
    layout = ...
    is_layouted = ...



# File: /apps/my_app/admin.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):

    readonly_fields = (
        "how_much_pages_has_my_site",
    )
    # All fields exclusively for the CMS Adding New object:
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "site_type",
                )
            },
        ),
        (
            "Conteúdo",
            {
                "fields": (
                    "layout",
                    "vue_component",  # May be removed dynamically if certain conds are met.
                )
            },
        ),
        ...
    )
    # All fields exclusively for the CMS Visualizing an object:
    fieldsets = (
        ...
        (
            "Configurações",
            {
                "fields": (
                    "config_1",  # May be removed dynamically if certain conditions are met.
                    "config_2",  # May be removed dynamically if certain conditions are met.
                    "config_3",  # May be removed dynamically if certain conditions are met.
                    "config_4",  # May be removed dynamically if certain conditions are met.
                    "config_5",  # May be removed dynamically if certain conditions are met.
                )
            },
        ),
        ...
    )

    # Example of a method field (not editable, just a information):
    def how_much_pages_has_my_site(self, obj):
        ...
        return ...

    # IMPORTANT: This method below is MANDATORY when we use add_fieldsets and fieldsets benefits:
    def get_fieldsets(self, request, obj=None):
        """Brings all data from fieldsets of the admin class."""
        
        # If you would have no field customizations:
        # return self.add_fieldsets if not obj else self.fieldsets

        # Convert tuple of tuples into mutable structure:
        fieldsets_list = []
        for title, opts in fieldsets:
            fields = list(opts.get("fields", []))
            # Only remove fields if editing an existing object:
            if obj and hasattr(obj, "site_type"):
                match obj.site_type:
                    case "b2b":
                        for field in ["config_1", "config_2"]:
                            if field in fields:
                                fields.remove(field)
                    case "b2c":
                        for field in ["config_1", "config_3", "config_5"]:
                            if field in fields:
                                fields.remove(field)
                    case "c2c":
                        for field in ["config_2", "config_4"]:
                            if field in fields:
                                fields.remove(field)

            fieldsets_list.append((title, {**opts, "fields": tuple(fields)}))
        return fieldsets_list


    # ANOTHER EXAMPLE:
    def get_fieldsets(...):
        # If it's in singleton creation step, escape this method:
        if obj is None:
            return self.add_fieldsets
        # Otherwise, convert tuple of tuples into mutable structure:
        fieldsets = list(self.fieldsets)
        # Check if the right attribute exists, and if Vue isn't the external front-end solution:
        if obj and hasattr(obj, "front_type") and obj.front_type != consts.VAL_FRONT_TOOL_VUE:
            fieldsets_list = []
            for title, opts in fieldsets:
                fields = list(opts.get("fields", []))
                field = "vue_pg_comps_path"
                if field in fields:
                    fields.remove(field)
                # Rebuild fieldset with updated fields:
                fieldsets_list.append((title, {**opts, "fields": fields}))
            fieldsets = fieldsets_list