from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models
from django.db.models.functions import Length

from django.conf import settings as stgs

from . import constants as consts
from . import validators
from .utils_models import pagex_slugifier


class PagexKeyword(models.Model):
    """Only through CMS, it manages which keywords are available to be associated with Pagex,
    providing more SEO information for Search Engines like Google."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    kw = models.CharField(
        max_length=consts.VAL_KEYWORD_MAX,
        unique=True,
        verbose_name="Palavra-chave",
        validators=[
            MinLengthValidator(consts.VAL_KEYWORD_MIN),
            MaxLengthValidator(consts.VAL_KEYWORD_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_SEO_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,
        verbose_name="Identificador",
    )

    class Meta:
        db_table = "pagex_keyword"
        ordering = ["kw"]
        verbose_name = "3. Palavra-chave"
        verbose_name_plural = "3. Palavras-chave"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    kw__length__range=(consts.VAL_KEYWORD_MIN, consts.VAL_KEYWORD_MAX)
                ),
                name="kw_length",
            ),
        ]

    def __str__(self):
        return self.kw

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        if self.kw.strip():
            self.kw = self.kw.lower()
            self.slug = pagex_slugifier(self.kw)
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""
        if self.kw:
            result1 = validators.clean_checker_txt_uniqueness(
                PagexKeyword, self, "kw", self.kw, True, "lower"
            )
            result2 = validators.clean_checker_txt_uniqueness(
                PagexKeyword, self, "slug", self.slug, False, ""
            )
            if result1 and result2:
                self.kw = result1
                self.slug = result2


class PagexCategory(models.Model):
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
        help_text="Categoria a ser utilizada para agrupar páginas do portal.",
        validators=[
            MinLengthValidator(consts.VAL_CAT_MIN),
            MaxLengthValidator(consts.VAL_CAT_MAX),
            validators.validate_chars_spaces_enabled,
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_SEO_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,
        verbose_name="Identificador",
    )

    class Meta:
        db_table = "pagex_category"
        ordering = ["cat"]
        verbose_name = "3. Categoria"
        verbose_name_plural = "3. Categorias"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(cat__length__range=(consts.VAL_CAT_MIN, consts.VAL_CAT_MAX)),
                name="cat_length",
            ),
        ]

    def __str__(self):
        return self.cat

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        if self.cat.strip():
            # self.cat = self.cat.title()  # In this case, leave it for the user!
            self.slug = pagex_slugifier(self.cat)
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""
        if self.cat:
            result1 = validators.clean_checker_txt_uniqueness(
                PagexCategory, self, "cat", self.cat, True, "lower"
            )
            result2 = validators.clean_checker_txt_uniqueness(
                PagexCategory, self, "slug", self.slug, False, ""
            )
            if result1 and result2:
                self.kw = result1
                self.slug = result2


class PagexRedirection(models.Model):
    """Stores custom URL redirection links that can be used in menus."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_TITLE_MAX,
        unique=True,
        blank=False,
        verbose_name="Nome",
        help_text="Nome que aparecerá nos menus onde este link estará presente.",
        validators=[
            MinLengthValidator(consts.VAL_TITLE_MIN),
            MaxLengthValidator(consts.VAL_TITLE_MAX),
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
        ordering = ["name"]
        verbose_name = "3. Redirecionamento"
        verbose_name_plural = "3. Redirecionamentos"

    def __str__(self):
        return f"{self.name} (Redirecionamento)"


class PagexPage(models.Model):
    """Only through CMS, it manages (including, excluding, updating) pages of the app."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    title = models.CharField(
        unique=True,  # Important: 'coz SEO Title could use Title as reference & that must be unique!
        max_length=consts.VAL_TITLE_MAX,
        blank=False,
        null=False,
        verbose_name="Título (Menus)",
        help_text="Título que será mostrado em menus da aplicação.",
        validators=[
            MinLengthValidator(consts.VAL_TITLE_MIN),
            MaxLengthValidator(consts.VAL_TITLE_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_SEO_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        db_index=True,
        # verbose_name="Link/URL",
        # help_text="URL baseada no Título (SEO). A criação/edição da URL é automática.",
    )
    categories = models.ManyToManyField(
        "PagexCategory",
        blank=True,
        related_name="pagex_categories",
        verbose_name="Categorias",
        help_text="Selecione uma ou mais categorias as quais esta página pertence. Se preferir, pode deixar em branco.",
    )
    seo_title = models.CharField(
        unique=True,  # Important: 'coz the Slug needs to be unique!
        max_length=consts.VAL_SEO_TITLE_MAX,
        blank=True,
        verbose_name="Título (SEO)",
        help_text="Título que aparecerá na barra de título do navegador e, principalmente, será usado na criação/edição da URL da página e na indexação dela em sites de busca. Se em branco, o Título usado nos menus será usado.",
        validators=[
            MinLengthValidator(consts.VAL_SEO_TITLE_MIN),
            MaxLengthValidator(consts.VAL_SEO_TITLE_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    seo_desc = models.TextField(
        max_length=consts.VAL_SEO_DESC_MAX,
        blank=True,
        verbose_name="Descrição (SEO)",
        help_text="Breve descrição do conteúdo/função desta página para ser utilizado em sites de busca. Se em branco, o site de busca utilizará o primeiro parágrafo do Conteúdo da página, o que não garante uma boa apresentação.",
        validators=[
            MinLengthValidator(consts.VAL_SEO_DESC_MIN),
            MaxLengthValidator(consts.VAL_SEO_DESC_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    seo_keywords = models.ManyToManyField(
        "PagexKeyword",
        blank=True,
        related_name="pages",
        verbose_name="Palavras-chave (SEO)",
        help_text="O ideal é 1 única palavra ou termo-chave, mas você pode usar até 3. Isto ajuda na indexação da página em sites de busca. Se você adicionar mais de 3, sites de busca poderão ignorar todas as palavras-chave adicionadas.",
    )
    # This field value is managed by PagexSettings:
    is_home = models.BooleanField(
        default=False,
        verbose_name="É Página Inicial",
        help_text="Se esta página é a inicial do site. Configuração gerenciada através da Configurações de páginas.",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Criada em",
    )
    created_by = models.ForeignKey(
        stgs.AUTH_USER_MODEL,
        editable=False,
        related_name="pages",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Criada por",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Atualizada em",
    )
    updated_by = models.ForeignKey(
        stgs.AUTH_USER_MODEL,
        editable=False,
        related_name="updated_pages",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Atualizada por",
    )

    class Meta:
        db_table = "pagex_page"
        ordering = ["-is_home", "title"]
        verbose_name = "3. Página"
        verbose_name_plural = "3. Páginas"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    title__length__range=(consts.VAL_TITLE_MIN, consts.VAL_TITLE_MAX)
                ),
                name="page_title_length",
            ),
        ]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        # CRITICAL - DON'T change is_home value via PagexPage. MUST be managed by PagexSettings!

        # Minimum to validate:
        if self.title:
            # If SEO Title empty, define it based on Title:
            if not self.seo_title.strip():
                self.seo_title = self.title.strip()
            # Otherwise, force SEO title to update:
            else:
                self.seo_title = self.seo_title.strip()
            # Defining the slug based on SEO Title:
            self.slug = pagex_slugifier(self.seo_title)
            # Handle user tracking:
            user = kwargs.pop("user", None)  # Retrieve user from kwargs, default=None if not passed
            if user:
                if not self.pk:
                    self.created_by = user
                elif user.is_authenticated:
                    self.updated_by = user
            # LOG:
            self._log(user)
            # Save instance first to get ID for many-to-many relationships know the instance ID/PK:
            # CRUCIAL: don't move this save 'cause without it, adding PagexPage via CMS might fail!
            super().save(*args, **kwargs)

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

    def keyword_converter(self, txt_to_kw):
        """Convert a coma-separated string of keywords into a list of keywords."""
        if not txt_to_kw:
            return
        # Clear existing keywords:
        self.seo_keywords.clear()
        # Split the text by commas and strip whitespace:
        keywords = [kw.strip() for kw in txt_to_kw.split(",") if kw.strip()]
        # Create or get each keyword and add to the page:
        for kw in keywords:
            keyword, _ = PagexKeyword.objects.get_or_create(kw=kw)
            self.seo_keywords.add(keyword)

    def clean(self):
        """Built-in Model method used to provide custom model-level validation logic, and is called by full_clean() before save() the instance."""
        if self.title:
            result1 = validators.clean_checker_txt_uniqueness(
                PagexPage, self, "title", self.title, False, ""
            )
            if result1:
                self.title = result1

            if self.seo_title:
                result2 = validators.clean_checker_txt_uniqueness(
                    PagexPage, self, "seo_title", self.seo_title, False, ""
                )
                if result2:
                    self.seo_title = result2

            if self.slug:
                result3 = validators.clean_checker_txt_uniqueness(
                    PagexPage, self, "slug", self.slug, False, ""
                )
                if result3:
                    self.slug = result3


class PagexMenu(models.Model):
    """Only through CMS, it manages which Menus exist through the app, and which Pages and/or
    Categories are available for each one of them."""

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name = models.CharField(
        max_length=consts.VAL_MENU_MAX,
        unique=True,
        db_index=True,
        verbose_name="Nome",
        help_text="Nome do menu. Este nome é apenas uma identificação no CMS.",
        validators=[
            MinLengthValidator(consts.VAL_MENU_MIN),
            MaxLengthValidator(consts.VAL_MENU_MAX),
            validators.validate_chars_spaces_enabled,
        ],
    )
    identifier = models.SlugField(
        max_length=consts.VAL_MENU_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,
        verbose_name="Identificador",
    )

    class Meta:
        db_table = "pagex_menu"
        ordering = ["name"]
        verbose_name = "4. Menu"
        verbose_name_plural = "4. Menus"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(name__length__range=(consts.VAL_MENU_MIN, consts.VAL_MENU_MAX)),
                name="menu_name_length",
            ),
        ]

    def __str__(self):
        return f"{self.name} ({self.identifier})"

    def save(self, *args, **kwargs):
        """Built-in method that's executed when the entry saving runs."""
        if self.name.strip():
            self.name = self.name.strip().title()
            # Set the identifier based on the name:
            self.identifier = pagex_slugifier(self.name, is_underscore=True)  # Template friendly.
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
        related_name="links",
    )
    link_type = models.CharField(
        max_length=consts.VAL_LINK_TYPE_MAX,
        choices=consts.CHOICES_LINK_TYPE,
    )
    page = models.ForeignKey(
        "PagexPage",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="menu_links",
    )
    category = models.ForeignKey(
        "PagexCategory",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="menu_links",
    )
    redirection = models.ForeignKey(
        "PagexRedirection",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="menu_links",
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
        return "ERROR: Link sem destino"
