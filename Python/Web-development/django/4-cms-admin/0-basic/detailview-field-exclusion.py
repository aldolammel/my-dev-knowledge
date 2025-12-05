"""
    DJANGO CMS: EXCLUDING A FIELD IN DETAIL-VIEW

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
            "Configuraçoes",
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

    # IMPORTANT: This method below's MANDATORY when we use add_fieldsets and fieldsets benefits:
    def get_fieldsets(self, request, obj=None):
        """Brings all data from fieldsets of the admin class."""
        fieldsets = self.add_fieldsets if not obj else self.fieldsets
        # return fieldsets  # If you would have no field customizations!

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