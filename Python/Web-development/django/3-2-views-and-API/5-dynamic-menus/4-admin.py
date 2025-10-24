from django.contrib import admin
from . import forms, models


class PagexMenuLinkInline(SortableInlineAdminMixin, admin.StackedInline):
    model = models.PagexMenuLink
    form = forms.PagexMenuLinkForm
    extra = 0  # Control how many empty forms are displayed in the inline.
    # Define the fields to display in the inline admin:
    fields = ("combined_link",)
    # Specify the field to use for ordering:
    sortable_field_name = "position"


@admin.register(models.PagexMenu)
class PagexMenuAdmin(SortableAdminBase, admin.ModelAdmin):
    """Customizes the management of all menus used on the app."""

    # Custom form:
    # Reserved space...

    # Custom inlines:
    inlines = [PagexMenuLinkInline]

    list_display = (
        "name",
        "menu_link_counter",
        "json_link",  # instead of the original model class attribute "identifier".
    )
    # exclude = ()
    # filter_horizontal = ()
    # list_filter = ()
    search_fields = [
        "name",
    ]
    readonly_fields = ("identifier",)
    # All fields exclusively for the CMS Adding New object:
    # add_fieldsets = ()
    # All fields exclusively for the CMS Visualizing an object:
    # fieldsets = ()

    def menu_link_counter(self, obj):
        all_links = obj.links.all()
        # Count published and unpublished links of all link types:
        pub_count = 0
        unpub_count = 0

        for link in all_links:
            if link.link_type == "page" and link.page:
                if link.page.is_published:
                    pub_count += 1
                else:
                    unpub_count += 1
            elif link.link_type == "category" and link.category:
                # Check if the category has any published pages:
                if models.PagexPage.objects.filter(
                    categories=link.category, is_published=True
                ).exists():
                    pub_count += 1
                else:
                    # Category exists but has no published pages associated:
                    unpub_count += 1
            elif link.link_type == "redirection" and link.redirection:
                # Redirection links are always considered published
                pub_count += 1
        # Format the display:
        if unpub_count > 0:
            return format_html(
                "{} (+{} não publicado{})",
                pub_count,
                unpub_count,
                "s" if unpub_count > 1 else "",
            )
        else:
            return str(pub_count)

    menu_link_counter.short_description = "Nº de links"  # type: ignore[attr-defined]

    def json_link(self, obj):
        """Method to show the JSON data of the object."""
        url = ""
        if obj and obj.identifier:
            url = pagex_url_builder(obj, 4)
            return format_html("<a href='{}' target='_blank'>{}</a>", url, obj.identifier)
        return "ERROR: JSON não disponível!"

    json_link.short_description = "JSON"  # type: ignore[attr-defined]


@admin.register(models.PagexCategory)
class PagexCategoryAdmin(admin.ModelAdmin):
    """Customizes the management of page's categories. Categories can be also a link in application menus."""

    list_display = (
        "cat",
        "page_link",  # instead of 'slug'
    )
    search_fields = [
        "cat",
    ]

    # Create a hyperlink to the associated Slug to be used on the list-view:
    def page_link(self, obj):
        """To show the Slug with the category preview on list-view:"""
        url = pagex_url_builder(obj, 1, "category")
        if url:
            return format_html("<a href='{}' target='_blank'>{}</a>", url, obj.slug)
        return "ERROR: Ainda não há link para esta categoria!"

    # Create a hyperlink with help text for the detail-view:
    def page_link_with_help(self, obj):
        """To show the Slug with the category preview on detail-view:"""
        url = pagex_url_builder(obj, 1, "category")
        if url:
            return format_html(
                "<a href='{}' target='_blank'>{}</a><div class='help' style='margin: 0; padding-left: 0;'>URL baseada no campo Categoria. A criação/edição da URL é automática.</div>",
                url,
                obj.slug,
            )
        return "ERROR: Ainda não há link para esta página!"

    def get_readonly_fields(self, request, obj=None):
        """Built-in method to extend the 'readonly_fields' power."""
        if obj:
            # For Editing an existing object:
            return self.readonly_fields + ("page_link_with_help",)  # type: ignore[operator]
        # For Adding a new object:
        return self.readonly_fields

    # Defining this method label:
    page_link.short_description = "Visualizar"  # type: ignore[attr-defined]
    page_link_with_help.short_description = "Visualizar"  # type: ignore[attr-defined]


@admin.register(models.PagexRedirection)
class PagexRedirectionAdmin(admin.ModelAdmin):
    """Customizes the management of links' redirection for external application domains. Redirection links can be also a link in application menus."""

    list_display = (
        "name",
        "page_link",  # instead of 'url'!
        "is_new_tab",
    )
    list_filter = ("is_new_tab",)

    # Create a hyperlink to the associated URL to be used on the list-view:
    def page_link(self, obj):
        """To show the URL with link on list-view:"""
        if obj and obj.url:
            return format_html("<a href='{}' target='_blank'>{}</a>", obj.url, obj.url)
        return "ERROR: Ainda não há link para esta página!"



@admin.register(models.PagexPage)
class PagexPageAdmin(admin.ModelAdmin):
    """Customizes the management of each page registered through Pagex. Pages might be also links in app's navigation menus."""

    #...

    def save_model(self, request, obj, form, change):
        """It's a key part of Django's admin customization that allows you to control what happens
        when a model instance (models.py) is created/updated through the CMS."""
        # Then process the keywords if provided:
        if "txt_to_kw" in form.cleaned_data and form.cleaned_data["txt_to_kw"]:
            obj.keyword_converter(form.cleaned_data["txt_to_kw"])