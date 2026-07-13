#### Python > Django > Structure
# Models.py

---

*Django* is divided in 3 main parts: models, views, and templates. Models are responsible for listing the data structure of a Django app, using classes to build tables and their attributes in a database. Through *models.py* you:
- Define the schema of your database;
- Provide methods for querying and manipulating the data;
- Enforce data integrity by defining constraints and validations.

---
## Model-class example:
Django Model-class example that is used to create database structure: [/python/web-development/django/3-1-models-database/\_creating_db_table](/python/web-development/django/3-1-models-database/_creating_db_table.py)

---
## Common attribute-types:
Most common attribute-types you will use to build up each database field. Check how the model fields are interpreted by browsers:

models.CharField(max_length=40)
```
<input type="text">
```

models.TextField()
```
<textarea>
```

models.CharField(..., choices=(('v1', 'V 1'),('v2', 'V 2')), default='v1')
```
<select>
```

models.CharField(..., choices=(('v1', 'V 1'),('v2', 'V 2')), default='v1')
```
<input type="radio">
```

models.IntegerField(..., choices=((1, 'V 1'),(2, 'V 2')), default=1)
```
<select>
```

models.BooleanField() or NullBooleanField() <- when null=True
```
<boolean>
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="button">
```

models.ManyToMany()
```
<input type="checkbox">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="color">
```

models.DateField(auto_now_add=True)
```
<input type="date">
```

models.DateTimeField(auto_now_add=True)
```
<input type="datetime-local">
```

models.EmailField()
```
<input type="email">
```

models.FileField(default='', upload_to='/%Y/%m/%d/', max_length=100)
```
<input type="file">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="hidden">
```

models.ImageField(default='pholder.png', upload_to='/%Y/%m/%d/')
```
<input type="image">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="month">
```

models.PositiveSmallIntegerField()
```
<input type="number">
```

models.PositiveIntegerField()
```
<input type="number">
```

models.PositiveBigIntegerField()
```
<input type="number">
```

models.IntegerField()
```
<input type="number">
```

models.FloatField()
```
<input type="number">
```

models.DecimalField()
```
<input type="number">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="password">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="range">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="reset">
```

xxxxxxxxxxxxxxxxxxxxxxxxx 
```
<input type="search">
```

xxxxxxxxxxxxxxxxxxxxxxxxx 
```
<input type="submit">
```

xxxxxxxxxxxxxxxxxxxxxxxxx 
```
<input type="tel">
```

models.TimeField(auto_now_add=True)
```
<input type="time">
```

models.DurationField()
```
<input type="time">
```

models.URLField(unique=True, default='', db_index=True)
```
<input type="url">
```

models.SlugField(unique=True, default='', db_index=True)
```
<input type="url">
```

xxxxxxxxxxxxxxxxxxxxxxxxx
```
<input type="week">
```

---
## Form fields, including widget fields:
[/python/web-development/django/9-forms/\_forms_knowledge](/python/web-development/django/9-forms/_forms_knowledge.md)

---
## *Charfield* VS *Textfield*

*CharField* demands a max_length. E.g. name = models.CharField(max_length=40)

*TextField* is free for large amount of text. E.g. day_note = models.TextField(max_length=1200)

---
## Understanding the model field arguments (parameters):

E.g. models.CharField(arg1, arg2, ...)

[/python/web-development/django/3-1-models-database/2-model-arguments](/python/web-development/django/3-1-models-database/2-model-arguments.md)

---
## Renaming a class model:

Pay attention, following this checklist to avoid crashes widely in your app: [/python/web-development/django/3-1-models-database/renaming-model-class](/python/web-development/django/3-1-models-database/renaming-model-class.md)

---

**OTHER DJANGO PARTS:**
- Views: [/python/web-development/django/3-2-views-and-API/\_about](/python/web-development/django/3-2-views-and-API/_about.md)
- Templates: [/python/web-development/django/3-3-frontend-templates/\_about](/python/web-development/django/3-3-frontend-templates/_about.md)

