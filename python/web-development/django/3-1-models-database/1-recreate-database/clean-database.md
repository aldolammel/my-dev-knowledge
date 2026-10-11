#### Python > Django:
# Clean the database using `flush` command:

---
   
This command clears all data from all tables in our Django database, preserving the tables and columns only:

---
## Before: 

- If your app is multilingual and are using `prefix_language` mandatory, your new db must be created and, right after, you must include on language table at least one language for you be able to use the CMS! So be aware of this!

---
## 1) Flushing the db:

Using UV:
```bash
uv run manage.py flush
```
Or using Python only:
```bash
python manage.py flush
```

---
## 2) Probably you should delete all migration files from `migrations` folders!

---
## 3) Run `makemigrations` and `migrate` commands again!

---
## 4) Create your admin user again:
[/python/web-development/django/3-1-models-database/0-installing-and-adminUser/creating-admin-user](/python/web-development/django/3-1-models-database/0-installing-and-adminUser/creating-admin-user.md)

---
## 5) Test it:
Check if Django is okay: [/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---
## Case you realize you do need to recreate the database from scratch:
[/python/web-development/django/3-1-models-database/1-recreate-database/\_recreating-db](/python/web-development/django/3-1-models-database/1-recreate-database/_recreating-db.md)

