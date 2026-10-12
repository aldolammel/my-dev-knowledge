#### Python > Class types
# Abstract class

---

**Before:**
1. Abstract class concept: [/dev-concepts/class-type-abstract](/dev-concepts/class-type-abstract.md)
2. What is Model meta: [python/python-knowledge/classes/meta](python/python-knowledge/classes/meta.md)

---

Marks a model as a base class for inheritance, not a database table.

**When to use:**
- To create reusable model components/[mixins](dev-concepts/class-type-mixin.md);
- For shared fields or methods across multiple models;
- To implement design patterns (like BaseModel with common fields);
- The abstract model itself doesn't get a database table.

E.g.
- Mixin class: [python/web-development/django/3-1-models-database/model-type-mixin](python/web-development/django/3-1-models-database/model-type-mixin.md)
- Base model class: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

==Aware!==
- Abstract models SHOULDN'T have a primary key!

---
## When you CANNOT use abstract:

You cannot use an abstract model directly in a ForeignKey or ManyToManyField, even with a '*through=*' model. Django's ORM simply doesn't allow it 'cause abstract models are not installed in the database, so there's no concrete table to point to.

**Possible solution > Concrete Model:** [/python/web-development/django/3-1-models-database/\_model-class-model.py](/python/web-development/django/3-1-models-database/_model-class-model.py)

- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

MODEL'S INHERITANCE IN DJANGO:

[/python/web-development/django/3-1-models-database/Inheriting-attributes](/python/web-development/django/3-1-models-database/Inheriting-attributes.md)

WHAT IS MODEL META:

[python/python-knowledge/classes/meta](python/python-knowledge/classes/meta.md)