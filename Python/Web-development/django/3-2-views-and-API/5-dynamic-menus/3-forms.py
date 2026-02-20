from django import forms

from .models import (
    PagexCategory,
    PagexMenuLink,
    PagexPage,
    PagexRedirection,
)

class PagexMenuLinkForm(forms.ModelForm):
    """Customizing the Menu detail-view in the CMS."""

    # Custom combined field for pages and categories:
    combined_link = forms.ChoiceField(
        choices=[],
        label="Options",
        required=False,
    )

    class Meta:
        model = PagexMenuLink  # Form tied to this model.
        fields = [
            "combined_link",
        ]

    # Extra form fields (Not tied to the model):
    # Reserved space...

    def __init__(self, *args, **kwargs):
        """Dunder method called 'constructor' that runs automatically when a class instance is created."""
        super().__init__(*args, **kwargs)
        # Populate the choices with pages and categories:
        page_choices = [
            (f"page_{page.id}", f"{page.title} (Página)")
            for page in PagexPage.objects.filter(is_published=True)
        ]
        # Get categories and check if they have published pages:
        category_choices = []
        for cat in PagexCategory.objects.all():
            has_published_pages = PagexPage.objects.filter(
                categories=cat, is_published=True
            ).exists()
            if has_published_pages:
                category_choices.append((f"category_{cat.id}", f"{cat.cat} (Categoria)"))
            else:
                category_choices.append(
                    (
                        f"category_{cat.id}",
                        f"{cat.cat} (Atenção: categoria ainda vazia!)",
                    )
                )
        # Get redirection links:
        redirection_choices = [
            (f"redirection_{redirection.id}", f"{redirection.name} (Redirecionamento)")
            for redirection in PagexRedirection.objects.all()
        ]
        # Add an empty choice as the first option:
        empty_choice = [("", "---------")]
        # Combine all choices:
        all_choices = empty_choice + page_choices + category_choices + redirection_choices
        # Set initial value if editing an existing link:
        instance = kwargs.get("instance")
        if instance:
            if instance.link_type == "page" and instance.page:
                # Check if the page is still published:
                if not instance.page.is_published:
                    # Add a special choice for this unpublished page:
                    unpublished_choice = [
                        (
                            f"page_{instance.page.id}",
                            f"{instance.page.title} (Atenção: página não publicada ainda!)",
                        )
                    ]
                    all_choices = (
                        empty_choice
                        + unpublished_choice
                        + page_choices
                        + category_choices
                        + redirection_choices
                    )
                self.fields["combined_link"].initial = f"page_{instance.page.id}"
            elif instance.link_type == "category" and instance.category:
                self.fields["combined_link"].initial = f"category_{instance.category.id}"
            elif instance.link_type == "redirection" and instance.redirection:
                self.fields["combined_link"].initial = f"redirection_{instance.redirection.id}"
        # Important: the line below is perfect! Just a MyPy false-positive case:
        self.fields["combined_link"].choices = all_choices  # type: ignore[attr-defined]

    def save(self, commit=True):
        """Built-in Form method persists form data to the db."""
        instance = super().save(commit=False)
        # Parse the selected value to determine link type and object
        link_value = self.cleaned_data["combined_link"]
        # Handle empty selection:
        if not link_value:
            return instance
        try:
            link_type, object_id = link_value.split("_", 1)
            instance.link_type = link_type
            if link_type == "page":
                instance.page_id = object_id
                instance.category = None
                instance.redirection = None
            elif link_type == "category":
                instance.category_id = object_id
                instance.page = None
                instance.redirection = None
            elif link_type == "redirection":
                instance.redirection_id = object_id
                instance.page = None
                instance.category = None
            if commit:
                instance.save()
        except ValueError:
            # If there's an error splitting the value, don't save:
            if commit:
                instance.delete()
        return instance

