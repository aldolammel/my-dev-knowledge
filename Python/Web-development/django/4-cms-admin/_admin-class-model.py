@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    '''Customizing the management of xxxxxxxxxxxxxxxxx'''

    # Custom form:
    # Reserved space...

    # Custom form template:
    # Automatically searches as: /apps/your_app/templates/admin/your_app/model_name/change_form.html
    # E.g. /Python/Web-development/django/9-forms/change_form.html
    # For explicit path:
    # change_form_template = "admin/your_app/model_name/change_form.html"

    # Custom inlines:huSpUsa$r7_ex3s9
    # Reserved space...

    list_display = (
        "xxxxxxx",
    )
    # exclude = ()
    # filter_horizontal = ()
    # list_filter = ()
    # search_fields = []
    # readonly_fields = ()
    # All fields exclusively for the CMS Adding New object:
    # add_fieldsets = ()  # If you to use this, it demands get_fieldsets:
        # /Python/Web-development/django/4-cms-admin/method-get_fieldsets.py
    # All fields exclusively for the CMS Visualizing an object:
    # fieldsets = ()  # If you to use this, it demands get_fieldsets:
        # /Python/Web-development/django/4-cms-admin/method-get_fieldsets.py

    # If you have audit fields like 'created_by' or 'updated_by' you need save_model method:
    def save_model(self, request, obj, form, change):
        '''Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface.'''
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)