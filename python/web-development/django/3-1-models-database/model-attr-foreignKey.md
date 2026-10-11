#### Python > Django > Models > Field Classes (Attribute types)
# ForeignKey()

---

==Crucial==
It's not a field. It's just a reference to another class/table.

**Common Usage:**
Defining a many-to-one relationship between two models. It creates a database foreign key from one table to another's primary key.

**Field look-like on front-end:**
Depends of the original field class it calls.

## Examples:
```python
from django.conf import settings

# BlogPost model where many posts can be owned just by one author:
created_by = models.ForeignKey(
	settings.AUTH_USER_MODEL,
	editable=False,
	related_name="posts",
	on_delete=models.SET_NULL,
	null=True,
)
```

```python
# The same, but only logic:
<AttrOfModelA> = models.ForeignKey(
	<ModelB>,                                      # or between quotes if model comes later!
	editable=False,
	related_name="<WhatExactlyModelBownedHere+s>",                  # ./arg-related_name.txt
	on_delete=models.SET_NULL,
	null=True,
)
```

---
## OTHER RELATED OPTIONS:
Many-To-Many Field: [/python/web-development/django/3-1-models-database/model-attr-field-many-to-many](/python/web-development/django/3-1-models-database/model-attr-field-many-to-many.md)
## All Django field class (class attribute):
[/python/web-development/django/3-1-models-database/model-attr-field_all](/python/web-development/django/3-1-models-database/model-attr-field_all.md)



    