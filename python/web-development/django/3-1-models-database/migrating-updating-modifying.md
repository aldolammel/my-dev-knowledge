#### Python > Django > Models
# Modifying the db through changes in `models.py`

---

If you perform any modification in a `models.py`, you must execute a migration again. It tells to the database its schema must be changed:
### 1) Make Django translate the changes to SQL instruction
For all current sub-apps:
```bash
uv run manage.py makemigrations
# or 
python manage.py makemigrations
```
Or for a specific one:
```bash
uv run manage.py makemigrations <subapp_name>
# or
python manage.py makemigrations <subapp_name>
```
### 2) Asks Django to use the latest instruction to modify the db:
```bash
uv run manage.py migrate
# or 
python manage.py migrate
```

---
## Golden tips

### Modifying a ForeigKey() to ManyToManyField()
Django can’t `AlterField` from FK to M2M. So the solution is to comment the *ForeigKey()* attribute (and comment this field in admin.py if it exists in there) and run `makemigrations`. After that, uncomment it and modify it to *ManyToManyField()* as need. 
### Renaming a class model
Pay attention, following this checklist to avoid crashes widely in your app: [/python/web-development/django/3-1-models-database/renaming-model-class](/python/web-development/django/3-1-models-database/renaming-model-class.md)


