from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.db.models.functions import Length

from django.conf import settings as stgs

from . import consts
from . import validators
from .utils_models import pagex_slugifier

models.CharField.register_lookup(Length)


class PagexTag(models.Model):
    """Only through CMS, it manages which tags are available to be associated with Pagex,
    providing more SEO information for Search Engines like Google."""

    id = models.AutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_TAG_MAX,
        unique=True,
        verbose_name="Tag",
        help_text="Palavra ou expressão que descreva seus conteúdos de forma granular, mais específica que categorias, ajudando buscadores a encontrar seu conteúdo.",
        validators=[
            MinLengthValidator(consts.VAL_TAG_MIN),
            MaxLengthValidator(consts.VAL_TAG_MAX),
            validators.validate_chars_spaces_enabled,
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_TAG_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,  # Auto-generated in save().
        blank=True,  # Once it's auto-generated in save(), it'll pass empty for clean().
        verbose_name="Link/URL",
        help_text="URL automaticamente criada com base no título da tag.",
    )

    class Meta:
        db_table = "pagex_tag"
        ordering = ["name"]
        verbose_name = lang.meta_tag
        verbose_name_plural = lang.meta_tag
        constraints = [
            models.CheckConstraint(
                condition=models.Q(name__length__range=(consts.VAL_TAG_MIN, consts.VAL_TAG_MAX)),
                name="tag_name_length",
            ),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Runs full validation before saving:
        self.full_clean()

        if self.name:
            self.slug = pagex_slugifier(self.name)
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Error if tag name is NOT unique ('cause it builds up the tag slug):
        if self.name:
            self.name = validators.clean_checker_txt_uniqueness(
                PagexTag, self, "name", self.name, True, "lower"
            )


class PagexCategory(AuditBase):
    """Only through CMS, it manages which categories are available to be associated with Pagex."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    cat = models.CharField(
        max_length=consts.VAL_CAT_MAX,
        unique=True,
        verbose_name="Categoria",
        help_text="Criando categorias e relacionando-as ao conteúdo de sua aplicação, você amplia a organização da informação, maximizando as chances de usuários e serviços de busca a encontrar o que procuram. Diferente das palavras-chave, categorias podem ser criadas de forma hierárquicas.",
        validators=[
            MinLengthValidator(consts.VAL_CAT_MIN),
            MaxLengthValidator(consts.VAL_CAT_MAX),
            validators.validate_chars_spaces_enabled,
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_CAT_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,  # Auto-generated in save().
        blank=True,  # Once it's auto-generated in save(), it'll pass empty for clean().
        verbose_name="Link/URL",
        help_text="URL automaticamente criada com base no título da categoria.",
    )

    class Meta:
        db_table = "pagex_category"
        ordering = ["cat", "updated_at"]
        verbose_name = lang.meta_cat
        verbose_name_plural = lang.meta_cat_plural
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cat__length__range=(consts.VAL_CAT_MIN, consts.VAL_CAT_MAX)),
                name="cat_length",
            ),
        ]

    def __str__(self):
        return self.cat

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Runs full validation before saving:
        self.full_clean()

        if self.cat:
            # self.cat = self.cat.title()  # In this case, leave it for the user!
            self.slug = pagex_slugifier(self.cat)
            # Tracking the current user:
            user = kwargs.pop("user", None)
            if user and user.is_authenticated:
                if not self.created_by:
                    self.created_by = user
                else:
                    self.updated_by = user
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Error if category title is NOT unique ('cause it builds up the slug):
        if self.cat:
            self.cat = validators.clean_checker_txt_uniqueness(
                PagexCategory, self, "cat", self.cat, True, "lower"
            )


class PagexRedirection(AuditBase):
    """Stores custom URL redirection links that can be used in menus."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_PAGE_TITLE_MAX,
        unique=True,
        blank=False,
        verbose_name="Nome",
        help_text="Nome que aparecerá nos menus onde este link estará presente.",
        validators=[
            MinLengthValidator(consts.VAL_PAGE_TITLE_MIN),
            MaxLengthValidator(consts.VAL_PAGE_TITLE_MAX),
            validators.validate_chars_spaces_enabled,
        ],
    )
    url = models.URLField(
        max_length=255,
        blank=False,
        verbose_name="URL",
        help_text="URL completa para redirecionamento (ex: https://exemplo.com.br).",
        # validators=[URLValidator()],  # Not need when using URLField!
    )
    is_new_tab = models.BooleanField(
        default=True,
        verbose_name="Abrir em nova aba",
        help_text="Recomendado abrir em nova aba se o link pertencer a outro domínio que não seja o atual desta aplicação.",
    )

    class Meta:
        db_table = "pagex_redirection"
        ordering = ["name", "updated_at"]
        verbose_name = lang.meta_redirect
        verbose_name_plural = lang.meta_redirect_plural

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Runs full validation before saving:
        self.full_clean()

        if self.name:
            # Tracking the current user:
            user = kwargs.pop("user", None)
            if user and user.is_authenticated:
                if not self.created_by:
                    self.created_by = user
                else:
                    self.updated_by = user
            super().save(*args, **kwargs)


class PagexPage(SectionManagerMixin, AuditBase):
    """It manages (including, excluding, updating) pages of the app."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    title = models.CharField(
        unique=True,  # Important: 'coz SEO Title could use Title as reference & that must be unique!
        max_length=consts.VAL_PAGE_TITLE_MAX,
        blank=False,
        null=False,
        verbose_name=lang.lbl_title_for_menus,
        help_text=lang.htxt_title_for_menus,
        validators=[
            MinLengthValidator(consts.VAL_PAGE_TITLE_MIN),
            MaxLengthValidator(consts.VAL_PAGE_TITLE_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_PAGE_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        editable=False,  # Auto-generated in save().
        blank=True,  # Once it's auto-generated in save(), it'll pass empty for clean().
        verbose_name=lang.lbl_slug_link,
        help_text=lang.htxt_slug_title_for_seo,
    )
    vue_pg_comp = models.CharField(
        max_length=consts.VAL_PAGE_TITLE_MAX,
        blank=True,
        default="",
        verbose_name=lang.lbl_vue_pg_comp,
        help_text=lang.htxt_vue_pg_comp,
    )
    categories = models.ManyToManyField(
        "PagexCategory",
        blank=True,
        related_name="pagex_page_cats",
        verbose_name=lang.lbl_cats,
        help_text=lang.htxt_cats,
    )
    seo_page_title = models.CharField(
        unique=True,  # Important: 'coz the Slug needs to be unique! If this is built by title, title is already unique, but the issue is if the user defines it. That's why this is True again.
        max_length=consts.VAL_SEO_TITLE_MAX,
        blank=True,  # If empty, this field will be based on title.
        default="",
        verbose_name=lang.lbl_seo_title,
        help_text=lang.htxt_seo_title,
        validators=[
            MinLengthValidator(consts.VAL_SEO_TITLE_MIN),
            MaxLengthValidator(consts.VAL_SEO_TITLE_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    seo_desc = models.TextField(
        max_length=consts.VAL_SEO_DESC_MAX,
        blank=True,
        verbose_name=lang.lbl_seo_desc,
        help_text=lang.htxt_seo_desc,
        validators=[
            MinLengthValidator(consts.VAL_SEO_DESC_MIN),
            MaxLengthValidator(consts.VAL_SEO_DESC_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    seo_tags = models.ManyToManyField(
        "PagexTag",
        blank=True,
        related_name="pagex_page_tags",
        verbose_name=lang.lbl_seo_tags,
        help_text=lang.htxt_seo_tags,
    )
    is_published = models.BooleanField(
        default=True,
        verbose_name=lang.lbl_is_published,
        help_text=lang.htxt_is_published,
    )
    # CRITICAL: This field value is managed by PagexSettings:
    is_home = models.BooleanField(
        default=False,
        editable=False,
        verbose_name=lang.lbl_is_home,
        help_text=lang.htxt_is_home,
    )
    is_blog = models.BooleanField(
        default=False,
        verbose_name=lang.lbl_is_blog,
        help_text=lang.htxt_is_blog,
    )

    class Meta:
        db_table = "pagex_page"
        ordering = ["-is_home", "title"]
        verbose_name = lang.meta_pg
        verbose_name_plural = lang.meta_pg_plural
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    title__length__range=(consts.VAL_PAGE_TITLE_MIN, consts.VAL_PAGE_TITLE_MAX)
                ),
                name="page_title_length",
            ),
        ]

    def __str__(self):
        return self.title or f"{lang.tag_e} PagexPage.title"

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # CRITICAL - DON'T change is_home value via PagexPage. MUST be managed by PagexSettings!
        # Runs full validation before saving:
        self.full_clean()
        # If no seo title defined, copy the title already uniqueness checked and always is equal or a shorter version of SEO title's maximum characters:
        if not self.seo_page_title:
            self.seo_page_title = self.title
        # Defining the slug based on SEO Title:
        self.slug = pagex_slugifier(self.seo_page_title)
        # Handle user tracking:
        user = kwargs.pop("user", None)  # Retrieve user from kwargs, default=None if not passed
        if user and user.is_authenticated:
            if not self.created_by:
                self.created_by = user
            else:
                self.updated_by = user
        # LOG:
        self._log(user)
        super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Error if page title is NOT unique ('cause SEO title CAN BE build up based on it):
        self.title = validators.clean_checker_txt_uniqueness(
            PagexPage, self, "title", self.title, False, ""
        )
        # Error if SEO title is NOT unique ('cause slug and good SEO demand it):
        if self.seo_page_title:
            # If user defined a seo title, check its uniqueness:
            self.seo_page_title = validators.clean_checker_txt_uniqueness(
                PagexPage, self, "seo_page_title", self.seo_page_title, False, ""
            )
        # Error if NO Pagex singleton:
        pagex_stgs = PagexSettings.objects.first()
        if not pagex_stgs:
            print(f"{consts.TAG_E} {lang.e_obj_404_pagex}")
            raise PagexSettings.DoesNotExist(f"{lang.tag_e} {lang.e_obj_404_pagex}")
        # Error if Vue is frontend solution but its required fields are empty:
        is_vue = pagex_stgs == consts.VAL_FRONT_TOOL_VUE
        if is_vue and not self.vue_pg_comp:
            raise ValidationError(
                {"vue_pg_comp": "Campo obrigatório quando o Tipo de Front-end for Vue.js."}
            )
        # Frontend external solution validations:
        # Vue:
        if is_vue:
            raise ValidationError(
                {
                    "vue_pg_comp": ValidationError("xxxxxxxxxxxxxxxxxxxxxx"),
                }
            )

    def add_section(self, section, pos=None):
        """Add a section to the page at specified position.
        section: PagexSection instance to add
        pos: Position where to insert (None = append at end)"""
        SectionManagerMixin.add_section(self, section, pos)

    def remove_section(self, section_order):
        """Remove all content entries for a specific section_order.
        section_order: The section_order value to remove"""
        # Use mixin implementation:
        return SectionManagerMixin.remove_section(self, section_order)

    def get_section_manager(self):
        """Return the content manager for this page."""
        return self.page_content

    def get_section_parent_kwargs(self):
        """Return the parent kwargs for PagexContent creation."""
        return {"page": self}

    def get_structured_content(self):
        """Returns page content organized by sections in their correct order."""
        content_entries = self.page_content.select_related(
            "section_element__section", "section_element__element"
        ).order_by("section_order", "element_order")
        # Group content by section_order:
        structured = {}
        for c in content_entries:
            section_key = c.section_order
            if section_key not in structured:
                # Handle case where section_element might be NULL:
                section_obj = c.section_element.section if c.section_element else None

                structured[section_key] = {
                    "section": section_obj,
                    "order": c.section_order,
                    "elements": [],
                }
            # Get the appropriate content field based on element type:
            # (Handle case where section_element might be NULL)
            element = c.section_element.element if c.section_element else None
            # Determine content value based on element type:
            if element:
                if isinstance(element, PagexElementImg):
                    content_value = c.element_content_file_img
                elif isinstance(element, PagexElementFile):
                    content_value = c.element_content_file_doc
                elif isinstance(element, PagexElementLink):
                    content_value = c.element_content_link
                else:  # TXT or default!
                    content_value = c.element_content_txt
            # Otherwise, the element was deleted, so use the stored content:
            else:
                # Determine type by checking which field has content:
                if c.element_content_file_img:
                    content_value = c.element_content_file_img
                elif c.element_content_file_doc:
                    content_value = c.element_content_file_doc
                elif c.element_content_link:
                    content_value = c.element_content_link
                else:
                    content_value = c.element_content_txt

            structured[section_key]["elements"].append(
                {
                    "element": element,
                    "order": c.element_order,
                    "content": content_value,
                    "element_key": c.element_key,
                }
            )
        return sorted(structured.values(), key=lambda x: x["order"])

    def reorder_section(self, old_pos, new_pos):
        """Move a section from old_pos to new_pos.
        old_pos: Current section_order
        new_pos: Desired section_order"""
        if old_pos == new_pos:
            return
        # Get all contents in the section to move
        section_contents = list(self.page_content.filter(section_order=old_pos))
        if not section_contents:
            return
        if old_pos < new_pos:
            # Moving down, shift intermediate sections up:
            self.page_content.filter(section_order__gt=old_pos, section_order__lte=new_pos).update(
                section_order=models.F("section_order") - 1
            )
        else:
            # Moving up, shift intermediate sections down:
            self.page_content.filter(section_order__gte=new_pos, section_order__lt=old_pos).update(
                section_order=models.F("section_order") + 1
            )
        # Update the moved section
        for c in section_contents:
            c.section_order = new_pos
            c.save(update_fields=["section_order"])

    def _log(self, user):
        """For log purposes."""
        if not self.pk:
            print(
                f"{consts.TAG_D} New page created > title: {self.title} | slug: {self.slug} | by {user}"
            )
        else:
            print(
                f"{consts.TAG_D} Page updated > title: {self.title} | slug: {self.slug} | id: {self.pk} | is_published: {self.is_published} | |by {self.updated_by}"
            )

    def tag_converter(self, txt_to_tag):
        """Convert a coma-separated string of tags into a list of tags."""
        if not txt_to_tag:
            return
        # Clear existing tags:
        self.seo_tags.clear()
        # Split the text by commas and strip whitespace:
        tags = [i.strip() for i in txt_to_tag.split(",") if i.strip()]
        # Create or get each tag and add to the page:
        for name in tags:
            tag, _ = PagexTag.objects.get_or_create(name=name)
            self.seo_tags.add(tag)


class PagexMenu(AuditBase):
    """Only through CMS, it manages which Menus exist through the app, and which Pages and/or
    Categories are available for each one of them."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_SLUG_NAME_MAX,
        unique=True,
        db_index=True,
        verbose_name="Nome",
        help_text="Nome do menu. Este nome é apenas uma identificação no CMS.",
        validators=[
            MinLengthValidator(consts.VAL_SLUG_NAME_MIN),
            MaxLengthValidator(consts.VAL_SLUG_NAME_MAX),
            validators.validate_chars_spaces_enabled,
        ],
    )
    slug_key = models.SlugField(
        max_length=consts.VAL_SLUG_NAME_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,
        verbose_name=lang.lbl_key,
        help_text="Identificador usado no front-end para chamar o menu. A chave é criada/editada automática baseada no nome do menu.",
    )

    class Meta:
        db_table = "pagex_menu"
        ordering = ["name", "updated_at"]
        verbose_name = lang.meta_menu
        verbose_name_plural = lang.meta_menu_plural
        constraints = [
            models.CheckConstraint(
                condition=models.Q(name__length__range=(consts.VAL_MENU_MIN, consts.VAL_MENU_MAX)),
                name="menu_name_length",
            ),
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Runs full validation before saving:
        self.full_clean()

        if self.name.strip():
            self.name = self.name.strip().title()
            # Set the slug_key based on the name:
            self.slug_key = pagex_slugifier(self.name, is_underscore=True)  # Template friendly.
            # Tracking the current user:
            user = kwargs.pop("user", None)
            if user and user.is_authenticated:
                if not self.created_by:
                    self.created_by = user
                else:
                    self.updated_by = user
            # Save the instance/db entry:
            super().save(*args, **kwargs)


class PagexMenuLink(models.Model):
    """Each instance is a link in the app menus, be it a category, page, or redirect."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    menu = models.ForeignKey(
        "PagexMenu",
        on_delete=models.CASCADE,
        related_name="pagex_menu_links",
    )
    link_type = models.CharField(
        max_length=consts.VAL_LINK_TYPE_MAX,
        choices=consts.CHOICES_LINK_TYPE,
        default=None,
    )
    page = models.ForeignKey(
        "PagexPage",
        on_delete=models.CASCADE,
        related_name="pagex_page_links",
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        "PagexCategory",
        on_delete=models.CASCADE,
        related_name="pagex_cat_links",
        null=True,
        blank=True,
    )
    redirection = models.ForeignKey(
        "PagexRedirection",
        on_delete=models.CASCADE,
        related_name="pagex_redirect_links",
        null=True,
        blank=True,
    )
    position = models.PositiveSmallIntegerField(default=0)
    parent = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        related_name="children",
        on_delete=models.SET_NULL,
        help_text="",
    )

    class Meta:
        db_table = "pagex_menu_link"
        ordering = ["position"]
        verbose_name = "Link"
        verbose_name_plural = "Links"

    def __str__(self):
        if self.link_type == "page" and self.page:
            return f"{self.page.title} ({self.link_type})"
        elif self.link_type == "category" and self.category:
            return f"{self.category.cat} ({self.link_type})"
        elif self.link_type == "redirection" and self.redirection:
            return f"{self.redirection.name} ({self.link_type})"
        return f"{lang.tag_e} {lang.e_custom_link_404}"
