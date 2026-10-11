#### Python > Django > Models
# Common attribute-types (field classes)

---

Most common field classes you got to build every class attributes (db columns of a db table):

| Field Classes (Class attributes) on Django Models.py                                                                                               | On Django Template it looks like             |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [CharField(max_length=40)](/python/web-development/django/3-1-models-database/model-attr-field-char.md)                                            | `<input type="text">`                        |
| [TextField()](/python/web-development/django/3-1-models-database/model-attr-field-text.md)                                                         | `<textarea>`                                 |
| [CharField(..., choices=(('v1', 'V 1'),('v2', 'V 2')), default='v1')](/python/web-development/django/3-1-models-database/model-attr-field-char.md) | `<select>`                                   |
| [CharField(..., choices=(('v1', 'V 1'),('v2', 'V 2')), default='v1')](/python/web-development/django/3-1-models-database/model-attr-field-char.md) | `<input type="radio">`                       |
| [IntegerField(..., choices=((1, 'V 1'),(2, 'V 2')), default=1)](/python/web-development/django/3-1-models-database/model-attr-field-integer.md)    | `<select>`                                   |
| [BooleanField()](/python/web-development/django/3-1-models-database/model-attr-field-boolean.md)                                                   | `<boolean>`                                  |
| [OneToOneField()](/python/web-development/django/3-1-models-database/model-attr-field-one-to-one.md)                                               | It depends???????                            |
| [ManyToMany()](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md)                                                | `<input type="checkbox">`                    |
| [DateField(auto_now_add=True)](/python/web-development/django/3-1-models-database/model-attr-field-date.md)                                        | `<input type="date">`                        |
| [DateTimeField(auto_now_add=True)](/python/web-development/django/3-1-models-database/model-attr-field-dateTime.md)                                | `<input type="datetime-local">`              |
| [EmailField()](/python/web-development/django/3-1-models-database/model-attr-field-email.md)                                                       | `<input type="email">`                       |
| [FileField(default='', upload_to='/%Y/%m/%d/', max_length=100)](/python/web-development/django/3-1-models-database/model-attr-field-file.md)       | `<input type="file">`                        |
| [ImageField(default='pholder.png', upload_to='/%Y/%m/%d/')](/python/web-development/django/3-1-models-database/model-attr-field-image.md)          | `<input type="image">`                       |
| [SmallIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-smallInteger.md)                                         | `<input type="number">`                      |
| [PositiveSmallIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveSmallInteger.md)                         | `<input type="number">`                      |
| [IntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-integer.md)                                                   | `<input type="number">`                      |
| [PositiveIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveInteger.md)                                   | `<input type="number">`                      |
| [PositiveBigIntegerField()](/python/web-development/django/3-1-models-database/model-attr-field-positiveBigInteger.md)                             | `<input type="number">`                      |
| [FloatField()](/python/web-development/django/3-1-models-database/model-attr-field-float.md)                                                       | `<input type="number">`                      |
| [DecimalField()](/python/web-development/django/3-1-models-database/model-attr-field-decimal.md)                                                   | `<input type="number">`                      |
| [SmallAutoField()](/python/web-development/django/3-1-models-database/model-attr-field-smallAuto.md)                                               | `<input type="number">`                      |
| [AutoField()](/python/web-development/django/3-1-models-database/model-attr-field-auto.md)                                                         | `<input type="number">`                      |
| [BigAutoField()](/python/web-development/django/3-1-models-database/model-attr-field-bigAuto.md)                                                   | `<input type="number">`                      |
| [UUIDField()](/python/web-development/django/3-1-models-database/model-attr-field-uuid.md)                                                         | `<input type="number">`                      |
| [TimeField(auto_now_add=True)](/python/web-development/django/3-1-models-database/model-attr-field-time.md)                                        | `<input type="time">`                        |
| [DurationField()](/python/web-development/django/3-1-models-database/model-attr-field-duration.md)                                                 | `<input type="time">`                        |
| [URLField()](/python/web-development/django/3-1-models-database/model-attr-field-url.md)                                                           | `<input type="url">`                         |
| [SlugField()](/python/web-development/django/3-1-models-database/model-attr-field-slug.md)                                                         | `<input type="url">`                         |
| [ForeignKey()](/python/web-development/django/3-1-models-database/model-attr-foreignKey.md)                                                        | Depends of the original field class it calls |
| [JSONField()](/python/web-development/django/3-1-models-database/model-attr-field-json.md)                                                         | ??????                                       |
|                                                                                                                                                    | `<input type="password">`                    |
|                                                                                                                                                    | `<input type="range">`                       |
|                                                                                                                                                    | `<input type="search">`                      |
|                                                                                                                                                    | `<input type="submit">`                      |
|                                                                                                                                                    | `<input type="week">`                        |
|                                                                                                                                                    | `<input type="tel">`                         |

---
## Which attribute type to use to Primary Key?
[python/web-development/django/3-1-models-database/creating-id](python/web-development/django/3-1-models-database/creating-id.md)

