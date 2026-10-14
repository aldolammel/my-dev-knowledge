#### Python > Django > Models > Field Classes (Attribute types)
# FileField()

---

**Common Usage:**
Handling file uploads.

**Field look-like on front-end:**
- Single upload field.

Example:
```python
class Plane(models.Model):
    manual = models.FileField(
        upload_to="planes/manuals/",
        blank=True,
        verbose_name="xxxxxx",
        help_text="",
    )
```

---
## Similar field classes:
xxxxxxxxxxxxxxxxxx
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)

