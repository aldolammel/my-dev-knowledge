from django import template

register = template.Library()

@register.filter
def get_attribute(obj, attr):
    """Custom template filter to get attributes dynamically. Cefalog uses this, for example,
    to export PDFs."""
    # For primary keys and foreign keys:
    value = getattr(obj, attr)
    # Check if it's a M2M relationship:
    if hasattr(value, 'all'):
        return ', '.join([str(i) for i in value.all()])
    return value