# A GOOD DEPENDENCY THAT RESOLVE POLYMORPHISM ISSUES:
# django-polymorphic

# - - - - but you can work without dependencies:

# CONCRETE MODEL BELOW:
# apps/pagex/models.py

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# ... your other imports

class AuditBase(models.Model):
    ...


class PagexElementBase(AuditBase):
    name = models.CharField(max_length=consts.VAL_PAGE_TITLE_MAX, unique=True, ...)
    css_class = models.CharField(max_length=consts.VAL_SEO_TITLE_MAX, blank=True)
    slug = models.SlugField(max_length=..., unique=True, editable=False)

    class Meta:
        abstract = True


# CONCRETE MODEL — THIS IS THE KEY
class PagexElement(models.Model):
    """Concrete model that serves as the 'registry' for all element types. All actual element types (Txt, Img, etc.) will have a OneToOneField to this. This allows us to have real ForeignKey/M2M relationships."""
    content_type = models.ForeignKey("contenttypes.ContentType", on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    name = models.CharField(max_length=consts.VAL_PAGE_TITLE_MAX)  # duplicated for query convenience
    slug = models.SlugField(max_length=..., unique=True)

    class Meta:
        verbose_name = "Elemento de Página"
        verbose_name_plural = "Elementos de Página"

    def __str__(self):
        return self.name

    # Optional: delegate common fields
    @property
    def css_class(self):
        return getattr(self.content_object, "css_class", "")


# Now update your concrete element models:
class PagexElementTxt(PagexElementBase):
    txt_content = models.TextField(blank=True)

    # This creates the link to the registry
    base_element = models.OneToOneField(
        PagexElement,
        on_delete=models.CASCADE,
        parent_link=True,
        related_name="text_element",
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Ensure the registry instance exists
        if not hasattr(self, "base_element"):
            PagexElement.objects.create(
                content_object=self,
                name=self.name,
                slug=self.slug,
            )