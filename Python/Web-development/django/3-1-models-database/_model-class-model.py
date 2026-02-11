"""
    WHICH MODEL CLASS MODEL YOU WANT?
        1. For common/Parent class;
        2. For Child class;

"""

# 1. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ExampleModel(models.Model):
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name_xxxxxx = models.CharField(
        max_length=consts.VAL_XXXXXXXXX_MAX,
        unique=True,
        verbose_name="XXXXXXX",
        help_text="xxxxxxxxxxxxxxxxxxxxxxxxxx",
        validators=[
            MinLengthValidator(consts.VAL_XXXXXXX_MIN),
            MaxLengthValidator(consts.VAL_XXXXXXXXXX_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_PAGE_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,
        verbose_name="Identificador",
    )

    class Meta:
        db_table = "pagex_xxxxxxxx"
        ordering = ["xxxxxx"]
        verbose_name = "x. xxxxxxx"
        verbose_name_plural = "x. xxxxxxxxxxxxxxx"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    xxxxxxx__length__range=(consts.VAL_XXXXXXX_MIN, consts.VAL_XXXXXXXXXX_MAX)
                ),
                name="xxxxxxx_length",
            ),
        ]

    def __str__(self):
        return self.xxxxxxxx

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        
        # Runs full validation before saving:
        self.full_clean()

        if self.xxxxxxx.strip():
            self.slug = pagex_slugifier(self.xxxxxxx)
            super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""

        if self.xxxxxxx:
            result = validators.clean_checker_txt_uniqueness(
                PagexSection, self, "xxxxxxx", self.xxxxxxx, True, "title"
            )
            if result:
                self.xxxxxxx = result



# 2. - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class ExampleModel(models.Model):
    '''Stores xxxxxxxxxxxxxxxxxxxxxxx.'''

    id = models.SmallAutoField(
        primary_key=True,
        unique=True,
        editable=False,
    )
    name_xxxxxx = models.CharField(
        max_length=consts.VAL_XXXXXXXXX_MAX,
        unique=True,
        verbose_name="XXXXXXX",
        help_text="xxxxxxxxxxxxxxxxxxxxxxxxxx",
        validators=[
            MinLengthValidator(consts.VAL_XXXXXXX_MIN),
            MaxLengthValidator(consts.VAL_XXXXXXXXXX_MAX),
            # validators.validate_chars_spaces_enabled,  # Freedom for this!
        ],
    )
    slug = models.SlugField(
        max_length=consts.VAL_PAGE_TITLE_MAX + consts.VAL_SLUG_ADD_LIMIT,
        unique=True,
        editable=False,
        verbose_name="Identificador",
    )

    class Meta:
        db_table = "pagex_xxxxxxxx"
        ordering = ["xxxxxx"]
        verbose_name = "x. xxxxxxx"
        verbose_name_plural = "x. xxxxxxxxxxxxxxx"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(
                    xxxxxxx__length__range=(consts.VAL_XXXXXXX_MIN, consts.VAL_XXXXXXXXXX_MAX)
                ),
                name="xxxxxxx_length",
            ),
        ]

    def __str__(self):
        return self.xxxxxxxx

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Reserved space for child saving logic...
        # Saving data (including changes in parent via this child) in the db:
        super().save(*args, **kwargs)

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""
        # Allows the parent class to execute full_clean() in this child too:
        super().clean()
        # Reserved space for child validations...
