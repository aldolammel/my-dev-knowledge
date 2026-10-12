#### Python > Django > Model matters
# Meta class: Managed

---

**Before:**
1. What is Model meta: [python/python-knowledge/classes/meta](python/python-knowledge/classes/meta.md)

---

Controls database table management by Django's migration system.

What is meta in this context: [meta](python/python-knowledge/classes/meta.md)

**When to use "managed = False":**
- When working with legacy databases or tables created outside Django;
- When you want Django to read from but not manage the table;
- Requires you to manually define fields matching the existing table structure;
- Django will:
	- NOT create the table via migrations;
	- NOT modify/alter the table schema;
	- Still allow querying via ORM;
	- Still generate serializers, admin, etc.


E.g.
[/python/web-development/django/3-1-models-database/creating-virtual-model](/python/web-development/django/3-1-models-database/creating-virtual-model.md)


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

