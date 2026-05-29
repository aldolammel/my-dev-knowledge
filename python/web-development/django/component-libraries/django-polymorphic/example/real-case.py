
# DJANGO-POLYMORPHIC: REAL CASE EXAMPLE


# BUILDING POLYMORPHIC MODELS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
# All models inheriting from your polymorphic models will be polymorphic as well.

from polymorphic.models import PolymorphicModel

class AuditBase(models.Model):  # Abstract model!

    created_at = ...
    updated_at = ...
    updated_by = ...

    class Meta:
        abstract = True

class PagexElementBase(PolymorphicModel, AuditBase):  # type: ignore[django-manager-missing]

    id = ..
    name = ...
    css_class = ...
    slug = ...

    class Meta:
        ...

    def __str__(self):
        ...

    def save(self, *args, **kwargs):
        self.full_clean()

        if self.name:
            ...
            super().save(*args, **kwargs)

    def clean(self):
        ...

class PagexElementLink(PagexElementBase):

    link_title = ...
    link_url = ...
    link_is_target_blank = ...

    class Meta:
        ...

    def __str__(self):
        ...

    def save(self, *args, **kwargs):
        if self.name:
            ...

    def clean(self):
        super().clean()
        ...


# IN ADMIN - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from polymorphic.admin import (
    PolymorphicChildModelAdmin,
    PolymorphicParentModelAdmin,
)

class SaveUserMixin:
    def save_model(self, request, obj, form, change):
        obj.save(user=request.user)

@admin.register(models.PagexElementBase)
class PagexElementAdmin(SaveUserMixin, PolymorphicParentModelAdmin):
    base_model = models.PagexElementBase
    child_models = (
        models.PagexElementTxt,  # The first on this tuple is treated as the default!
        models.PagexElementLink,
    )

    list_display = (
        "name",
        "slug",
        "element_type",  # instead of the not UX-friendly "polymorphic_ctype".
        "updated_at",
        "updated_by",
    )
    list_filter = ("updated_by",)

    @admin.display(description="Tipo", ordering="polymorphic_ctype")  # making it sortable on CMS!
    def element_type(self, obj):
        # Returning the child class' verbose name:
        return obj.polymorphic_ctype.model_class()._meta.verbose_name

@admin.register(models.PagexElementTxt)
class PagexElementTxtAdmin(SaveUserMixin, PolymorphicChildModelAdmin):
    base_model = models.PagexElementTxt
    show_in_index = False  # hide link from CMS home (sidebar menu still shown)

    list_display = (
        # "id",
        "name",
        # "css_class",
        #  "slug",
        # "txt_content",
        "updated_at",
        "updated_by",
    )
    # exclude = ()
    # filter_horizontal = ()
    list_filter = ("updated_by",)
    search_fields = [
        "name",
        "txt_content",
    ]
    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
        "updated_by",
    )
    # All fields exclusively for the CMS Adding New object:
    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                    # "slug",
                ],
            },
        ),
        (
            "Conteúdo",
            {
                "fields": [
                    "txt_content",
                ],
            },
        ),
        (
            "Configuração",
            {
                "fields": [
                    "css_class",
                ]
            },
        ),
    )
    # All fields exclusively for the CMS Visualizing an object:
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                    "slug",
                ],
            },
        ),
        (
            "Conteúdo",
            {
                "fields": [
                    "txt_content",
                ],
            },
        ),
        (
            "Configuração",
            {
                "fields": [
                    "css_class",
                ]
            },
        ),
        (
            "Controle",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                    "updated_by",
                ]
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        """Built-in method to retrieve a list of tuples, in which each tuple represents a fieldset on the admin form page."""
        # Defines which fieldsets to start from:
        return self.add_fieldsets if not obj else self.fieldsets

@admin.register(models.PagexElementLink)
class PagexElementLinkAdmin(SaveUserMixin, PolymorphicChildModelAdmin):
    base_model = models.PagexElementLink
    show_in_index = False

    list_display = (
        # "id",
        "name",
        # "css_class",
        # "slug",
        # "link_title",
        # "link_url",
        # "link_is_target_blank",
        "updated_at",
        "updated_by",
    )
    # exclude = ()
    # filter_horizontal = ()
    list_filter = ("updated_by",)
    search_fields = [
        "name",
        "link_title",
    ]
    readonly_fields = (
        "slug",
        "created_at",
        "updated_at",
        "updated_by",
    )
    # All fields exclusively for the CMS Adding New object:
    add_fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                ],
            },
        ),
        (
            "Conteúdo",
            {
                "fields": [
                    "link_title",
                    "link_url",
                ],
            },
        ),
        (
            "Configuração",
            {
                "fields": [
                    "link_is_target_blank",
                    "css_class",
                ]
            },
        ),
    )
    # All fields exclusively for the CMS Visualizing an object:
    fieldsets = (
        (
            None,
            {
                "fields": [
                    "name",
                    "slug",
                ],
            },
        ),
        (
            "Conteúdo",
            {
                "fields": [
                    "link_title",
                    "link_url",
                ],
            },
        ),
        (
            "Configuração",
            {
                "fields": [
                    "link_is_target_blank",
                    "css_class",
                ]
            },
        ),
        (
            "Controle",
            {
                "fields": [
                    "created_at",
                    "updated_at",
                    "updated_by",
                ]
            },
        ),
    )

    def get_fieldsets(self, request, obj=None):
        """Built-in method to retrieve a list of tuples, in which each tuple represents a fieldset on the admin form page."""
        # Defines which fieldsets to start from:
        return self.add_fieldsets if not obj else self.fieldsets