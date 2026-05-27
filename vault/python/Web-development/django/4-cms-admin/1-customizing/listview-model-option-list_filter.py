
"""
    DJANGO CMS > ADMIN MODEL OPTION: LIST_FILTER

    The list_filter is a ModelAdmin option that creates a sidebar with filter options in the change list page of the Django admin interface.

"""

# Basic structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...

    list_filter = (
        "is_published",
        "categories",
    )


# Customizing the data for the filter - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# admin.py:
class BlogPagesFilter(admin.SimpleListFilter):
    """Filter to show only pages where is_blog=True in the sidebar"""

    title = "Página de Publicação"  # Sidebar title
    parameter_name = "blog"  # URL parameter

    def lookups(self, request, model_admin):
        """Return only pages that are blogs"""
        blog_pages = models.PagexPage.objects.filter(is_blog=True)
        return [(page.id, page.title) for page in blog_pages]

    def queryset(self, request, queryset):
        """Filter posts by selected blog page"""
        if self.value():
            return queryset.filter(blog_id=self.value())
        return queryset

@admin.register(models.Example)
class ExampleAdmin(admin.ModelAdmin):

    ...

    list_filter = (
        BlogPagesFilter,  # Instead of 'blog'
        "is_published",
        "categories",
    )