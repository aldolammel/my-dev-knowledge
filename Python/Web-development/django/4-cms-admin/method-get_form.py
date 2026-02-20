
"""
    DJANGO CMS > METHODS: GET_FORM()

    The get_form() method returns the form class that will be used in a view or admin interface. So its key purposes:

    - Dynamically select which form class to use based on conditions.
    - Modify form behavior without creating multiple views.
    - Customize form validation or fields programmatically.

    >> Not exclusive for CMS:
        While commonly used in Django Admin for CMS customization, get_form is available in:
        - Class-based views (CreateView, UpdateView, FormView).
        - Django Admin (ModelAdmin.get_form()).
        - Generic editing views.

    >> Its usage in Views:
        .../django/3-2-views-and-API/method-get_form.py
"""

# Structure - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

class MyModelAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        """Built-in method to customize the form that's displayed in the interface."""
        form = super().get_form(request, obj, **kwargs)
        # Admin-specific customizations
        return form


# Common example - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django import forms as f

class PagexPostAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, change=False, **kwargs):
        """Built-in method to customize the form that's displayed in the interface."""
        form = super().get_form(request, obj, change, **kwargs)
        ...
        # Customizing the dropdown-menu "blog" foreignkey field:
        if "blog" in form.base_fields:
            # Removing default add/remove buttons, applying the simple ModelChoiceField:
            form.base_fields["blog"] = f.ModelChoiceField(
                queryset=models.PagexPage.objects.filter(
                    is_blog=True,
                    # is_published=True,  # Important: let the unpublished blogs be listed too!
                ),
                required=False,
                label="Página de publicação",
                help_text="Selecione a página que esta publicação pertence.",
            )
        return form