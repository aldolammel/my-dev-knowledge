@admin.register(models.ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    '''Customizing the management of xxxxxxxxxxxxxxxxx'''

    # Custom form:
    # Reserved space...

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
    # add_fieldsets = ()
    # All fields exclusively for the CMS Visualizing an object:
    # fieldsets = ()

    # If you have 'created_by' or 'updated_by' you definitely need this method:
    def save_model(self, request, obj, form, change):
        '''Built-in CMS method that allows you to customize what happens when a model is saved through the Django CMS interface.'''
        # Sending to models.py the current user in CMS:
        obj.save(user=request.user)