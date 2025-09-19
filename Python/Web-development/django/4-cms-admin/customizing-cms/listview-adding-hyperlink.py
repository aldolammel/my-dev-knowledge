'''
    ADDING HYPERLINK IN LIST-VIEW:

'''

# In an admin.py file:
from .models import MyModelClass


@admin.register(MyModelClass)
class MyModelClassAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'page_link',  # Replacing the original Model Class attribute called 'url'!
        'is_new_tab',
    )
    search_fields = [
        "name",
        # "url",
    ]

    # Create a hyperlink to the associated URL to be used on the list-view:
    def page_link(self, obj):
        """To show the URL with link on list-view:"""
        if obj and obj.url:
            return format_html("<a href='{}' target='_blank'>{}</a>", obj.url, obj.url)
        return 'ERRO: Ainda não há link para esta página!'