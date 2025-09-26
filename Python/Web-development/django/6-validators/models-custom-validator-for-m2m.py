
"""
    DJANGO > VALIDATIONS: CUSTOM MODEL VALIDATOR FOR M2M (SPECIAL CASE)

    Since this is a many-to-many field, we need to handle this differently than regular fields.
    There is ONLY one way to validate a m2m field, and it means do it just right AFTER the instance saving (yes, if user escape from browser without set the mandatory field, you got no that info)!

    >> For non-m2m fields:
        /Python/Web-development/django/6-validators/models-custom-validator.py

"""


# FILE: /apps/my_app/validators.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from django.core.exceptions import ValidationError

def validate_m2m_not_empty(value, thing: str = "item"):
    """Validates that at least one thing is selected.
    CRUCIAL: 'blank=False' in m2m model fields doesn't work! That's why this func!"""
    if not value.exists():
        raise ValidationError(f"Make sure you select at least one {thing}.")



# FILE: /apps/my_app/models.py - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from .validators import validate_m2m_not_empty

class ExampleModel(models.Model):
    # ...existing code...
    
    elements = models.ManyToManyField(
        PagexElement,
        through="...",
        related_name="...",
        validators=[validate_m2m_not_empty],
    )

    def clean(self):
        """Built-in method for adding custom validation logic before full_clean() or save()."""
        super().clean()
        # M2M fields demands an ID so it's impossible to validate if no instance id involved:
        if self.pk:
            validate_m2m_not_empty(self.elements, "element")