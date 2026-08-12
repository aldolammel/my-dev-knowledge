#### Python > Django:
# Clean the database using `flush` command:

---
   
This command clears all data from all tables in our Django database, preserving the tables and columns only:

---
## Before: 

- If your app is multilingual and are using `prefix_language` mandatory, your new db must be created and, right after, you must include on language table at least one language for you be able to use the CMS! So be aware of this!

---
## 1) Flushing the db:

Common:
```
python manage.py flush
python manage.py createsuperuser
```
Or Using UV:
```
uv run manage.py flush
uv run manage.py createsuperuser
```

---
## 2) Test the app!

---
## Case you realize you do need to recreate the database from zero:
[/python/web-development/django/3-1-models-database/1-recreate-database/\_recreating-db](/python/web-development/django/3-1-models-database/1-recreate-database/_recreating-db.md)

