"""
    DJANGO > UTILS: ALDO'S SLUGIFIER SOLUTION

    
"""


# apps/your_app/utils.py: - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

def better_slugifier(txt: str, is_underscore: bool = False, should_suffix: bool = False):
    """Extended Django slugify function to serve Pagex purposes. By @aldolammel."""
    from django.utils.text import slugify

    # Initial value:
    slugified = slugify(txt)
    # Traditional slug (common):
    if not is_underscore and not should_suffix:
        return slugified  # E.g. text-like-this
    # Special slugs:
    special_slugified = slugified.replace("-", "_")
    # Slug with underscore instead:
    if is_underscore and not should_suffix:
        return special_slugified  # E.g. text_like_this
    # Slug underscore with prefix:
    if is_underscore and should_suffix:
        from random import randint

        return f"{special_slugified}_{randint(20, 9999)}"  # E.g. text_like_this_3023
    else:
        print(f"{consts.TAG_E}: pagex_slugifier() has trying a forbidden setup!")
        return None


# How to use it in a models.py: - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class SomethingModel (...):
    name = models.CharField(...)
    slug = models.SlugField(...)

    def save(self, *args, **kwargs):
        """Built-in Model method that's executed when the db entry saving runs."""
        # Runs full validation before saving:
        self.full_clean()

        if self.name:
            self.slug = utils.better_slugifier(self.name)
            super().save(*args, **kwargs)

    
# Case you need an extra care about the uniqueness (in validators.py): - - - - - - - - -
#   clean_checker_txt_uniqueness: /python/web-development/django/3-1-models-database/2-forms-and-validations/uniqueness-of-a-name.py



# And then add this in that class you are using the slugifier: - - - - - - - - - - - - -

from . import validators

class SomethingModel (...):
    name = ...
    slug = ...

    def save(...):
        ...

    def clean(self):
        """Built-in Model method to cross-field custom validations at the model-level once the code explicit calls full_clean() before save() the instance."""

        if self.name:
            result = validators.clean_checker_txt_uniqueness(
                SomethingModel, self, "name", self.name, True, "lower"
            )
            if result:
                self.slug = result
