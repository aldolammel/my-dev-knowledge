#### Python > Django > Sub-apps
# Deleting an app (sub-app)

---

==Remember my statement:==
Personally, I call "app" as "sub-app", meanwhile for me an `app` is the project's product itself.

---
## Make a decision:

- 1A) If sub-app is NOT installed yet;
- 1B) Or if sub-app is installed;

......................................

### 1A) If sub-app is NOT installed yet

1A.1) Just delete the sub-app folder;

......................................

### 1B) If sub-app is installed

1B.1) Basicaly, in the sub-app folder, delete all classes/tables from its 'models.py';

1B.2) Make the same in 'admin.py' when needed. If other file is calling that classes,
make sure to delete that calls too, including in other sub-apps if needed too;

1B.3) Update your database with these changes:

# for all apps:
```bash
$ python manage.py makemigrations
```

# Or for a specific one:
```bash
$ python manage.py makemigrations <app_name>
```

1B.4) Check the database if all old tables were deleted;

1B.5) Run the application and check if everything is okay:
```bash
$ python manage.py runserver
# or
$ uv run manage.py runserver
```

1B.6) If everything is fine, apply the migration:
```bash
python manage.py migrate
```

1B.7) In core-folder, remove the sub-app path from the 'urls.py' file;

1B.8) Still in core-folder, remove the sub-app name from the 'settings.py' file;

1B.9) Delete the sub-app folder;

---
## Test the application again:
[/python/web-development/django/\_running-app](/python/web-development/django/_running-app.md)



