#### Python > Django > Models
# Common attribute-types (field classes)

---

Most common field classes you got to build every class attributes (db columns of a db table):

| Field Classes on Models.py                                                                                                                                | On Django Template it looks like           |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [CharField(max_length=40)](/python/web-development/django/3-1-models-database/model-attr-field-char.md)                                                   | `<input type="text">`                      |
| [TextField()](/python/web-development/django/3-1-models-database/model-attr-field-text.md)                                                                | `<textarea>`                               |
| [CharField(..., choices=(('v1', 'V 1'),('v2', 'V 2')), default='v1')](/python/web-development/django/3-1-models-database/model-attr-field-char.md)        | `<select>`                                 |
| [CharField(..., choices=(('v1', 'V 1'),('v2', 'V 2')), default='v1')](/python/web-development/django/3-1-models-database/model-attr-field-char.md)        | `<input type="radio">`                     |
| [IntegerField(..., choices=((1, 'V 1'),(2, 'V 2')), default=1)](/python/web-development/django/3-1-models-database/model-attr-field-integer.md)           | `<select>`                                 |
| [BooleanField()](/python/web-development/django/3-1-models-database/model-attr-field-boolean.md)                                                          | `<input type="checkbox">`                  |
| [OneToOneField()](/python/web-development/django/3-1-models-database/model-attr-field-one-to-one.md) (Django automatically create this when needed)       | `<select>` (single-selection only)         |
| OnToManyField() doesn't exist. The Many side always uses [ForeignKey()](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md) |                                            |
| [ForeignKey()](python/web-development/django/3-1-models-database/model-attr-field-foreignKey.md)                                                          | `<select>` (single-selection only)         |
| [ManyToManyField()](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md)                                                  | `<select multiple>`                        |
| ManyToManyField(MyModel, blank=True) with `CheckboxSelectMultiple` widget                                                                                 | `<input type="checkbox">` (one per choice) |
| [DateField(auto_now_add=True)](/python/web-development/django/3-1-models-database/model-attr-field-date.md)                                               | `<input type="date">`                      |
| [DateTimeField(auto_now_add=True)](/python/web-development/django/3-1-models-database/model-attr-field-dateTime.md)                                       | `<input type="datetime-local">`            |
| [EmailField()](/python/web-development/django/3-1-models-database/model-attr-field-email.md)                                                              | `<input type="email">`                     |
| [FileField(default='', upload_to='/%Y/%m/%d/', max_length=100)](/python/web-development/django/3-1-models-database/model-attr-field-file.md)              | `<input type="file">`                      |
| FilePathField(path='/path/to/files')                                                                                                                      | `<select>`                                 |
| [ImageField(default='pholder.png', upload_to='/%Y/%m/%d/')](/python/web-development/django/3-1-models-database/model-attr-field-image.md)                 | `<input type="file">`                      |
| [SmallIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-smallInteger.md)                                                | `<input type="number">`                    |
| [PositiveSmallIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveSmallInteger.md)                                | `<input type="number">`                    |
| [IntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-integer.md)                                                          | `<input type="number">`                    |
| [PositiveIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveInteger.md)                                          | `<input type="number">`                    |
| [PositiveBigIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveBigInteger.md)                                    | `<input type="number">`                    |
| [FloatField()](/python/web-development/django/3-1-models-database/model-attr-field-float.md)                                                              | `<input type="number">`                    |
| [DecimalField()](/python/web-development/django/3-1-models-database/model-attr-field-decimal.md)                                                          | `<input type="number">`                    |
| [SmallAutoField()](/python/web-development/django/3-1-models-database/model-attr-field-smallAuto.md)                                                      | `<input type="number">`                    |
| [AutoField()](/python/web-development/django/3-1-models-database/model-attr-field-auto.md)                                                                | `<input type="number">`                    |
| [BigAutoField()](/python/web-development/django/3-1-models-database/model-attr-field-bigAuto.md)                                                          | `<input type="number">`                    |
| [UUIDField()](/python/web-development/django/3-1-models-database/model-attr-field-uuid.md)                                                                | `<input type="text">`                      |
| [TimeField(auto_now_add=True)](/python/web-development/django/3-1-models-database/model-attr-field-time.md)                                               | `<input type="time">`                      |
| [DurationField()](/python/web-development/django/3-1-models-database/model-attr-field-duration.md)                                                        | `<input type="time">`                      |
| [URLField()](/python/web-development/django/3-1-models-database/model-attr-field-url.md)                                                                  | `<input type="url">`                       |
| [SlugField()](/python/web-development/django/3-1-models-database/model-attr-field-slug.md)                                                                | `<input type="text">`                      |
| [JSONField()](/python/web-development/django/3-1-models-database/model-attr-field-json.md)                                                                | `<textarea>`                               |
| [BinaryField()](/python/web-development/django/3-1-models-database/model-attr-field-binary.md)                                                            |                                            |
| IPAddressField()                                                                                                                                          | `<input type="text">`                      |
| GenericIPAddressField()                                                                                                                                   | `<input type="text">`                      |
| GeneratedField(expression=..., output_field=..., db_persist=True)                                                                                         |                                            |


---
## Which attribute type to use to Primary Key?
[python/web-development/django/3-1-models-database/creating-id](python/web-development/django/3-1-models-database/creating-id.md)
# Common attribute-types (form field classes):
[/python/web-development/django/9-forms/form-attr-field_all](/python/web-development/django/9-forms/form-attr-field_all.md)
