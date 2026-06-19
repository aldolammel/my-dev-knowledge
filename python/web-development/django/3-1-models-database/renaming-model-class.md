#### Python > Django > Model matters
# Renaming a model class safely

---

**1. Change the model class name in yourapp/models.py**;

**2. Search for all occurrences of that model class name and update all of them!**

**3. Careful because it's not done yet:**
Django has different patterns to call a model class in different situations. For example, your model class is called PagexElementBase. So, it can be used like these example below:

E.g.
```
# admin.py
url = reverse("admin:pagex_pagexelementbase_add")

# "admin:<yourappname_yourmodelclassname_...>"
```

**4. Update your database schema with the new data:**
```
uv run manage.py makemigrations
uv run manage.py migrate
```