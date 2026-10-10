#### Python > Django > Project types > Discovery
# Updating Django in a finished product

---
## Before:

1. [ ] Assuming you, at least, know the current Python installed: [/python/0-new-project/discovery-python](/python/0-new-project/discovery-python.md)
2. [ ] Assuming you have finished Django discovery: [/python/web-development/django/0-new-project/discovery-django](/python/web-development/django/0-new-project/discovery-django.md)
3. [ ] Did you obtain approval for this update/upgrade from the IT product lead/product leader through an official channel?
4. [ ] Assuming you already have done the system backup!
	- [Backup on PostgreSQL](/database/PostgreSQL/backup-on-postgresql.md)
	- [Backup on MariaDB](/database/MariaDB/backup-on-maria.md)
	- [Backup on MySQL](/database/MySQL/backup-on-mysql.md)
	- [Backup on SQLite](/database/SQLite/backup-on-sqlite.md)
	- [Backup on CassandraDB](/database/CassandraDB/backup-on-cassandra.md)
5. [ ] Assuming you already have done the files backup!

---
## 1) Updating it:

**Make a decision:**

- 1A) Using UV.
- 1B) Using Python/PIP.

......................................
### 1A) Using UV

**Before:**
1. Assuming you are activated in the right virtual environment.
2. Assuming you already have the UV installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

1A.1) Define which new version every dependency of the product need and pin them to the `pyproject.toml`!

1A.2) Update the `uv.lock` and `.python-version` dynamically, running again the UV sync: [/python/package-manager/uv/auto-installation-with-sync](/python/package-manager/uv/auto-installation-with-sync.md)

1A.3) Update the Django, going to the project folder and, e.g.:
```bash
uv add "django>=5.2.7,<5.3"
```
Check the `pyproject.toml` file if the new version was correctly declared!

1A.4) Update all dependencies to ensure compatibility with new Django version: [/python/package-manager/uv/upgrade-dependencies](/python/package-manager/uv/upgrade-dependencies.md)

1A.5) (If applicable) Execute the migration:
```bash
uv run manage.py migrate
```

......................................
### 1B) Using Python/PIP

**Before:**
1. Assuming you are activated in the right virtual environment.

1B.1) Define which dependency new version the product needs and pin them to the `requirements.txt`!

1B.x) xxxxxxxxxxxxxxxxxxxx

1B.x) xxxxxxxxxxxxxxxxxxxx

---
## 2) Test it:
[/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---
## 3) Once the Django is updated:
Finish this roadmap asking yourself if front-end shouldn't be updated/upgraded too: [/python/web-development/django/0-new-project/discovery-django](/python/web-development/django/0-new-project/discovery-django.md)

---
