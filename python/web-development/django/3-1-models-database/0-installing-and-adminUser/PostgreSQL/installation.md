#### Python > Django > Installing
# Using PostgreSQL

---

**Summary:**
1) Installing the db with its basic integration;
2) Integrating database and back-end;
3) Creating the database;

---
## 1) Installing the db with its basic integration

If the db won't be in the cloud, install it locally: [database/PostgreSQL/0-basic/1-installing-and-integrating](database/PostgreSQL/0-basic/1-installing-and-integrating.md)

---
## 2) Integrating database and back-end

**2.1) Install a Python lib for PostgreSQL:** 
- [python/component-libraries/psycopg/0-psycopg](python/component-libraries/psycopg/0-psycopg.txt)
- Case you need a *settings.py* template: [python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py](python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py)

**2.2) (If applicable) Make a copy of the '.env' file to your project root folder:** 
- [environment-variables/env-for-local/in-backend/.env](environment-variables/env-for-local/in-backend/.env)

**2.3) (If applicable) Delete the sqlite.db:**

If you see the file in the project root folder, delete it once you are using PostgreSQL and you have no data from this project in that SQLite.

---
## 3) Creating the db

==Attention!==
If you are installing a new Django project, return to the previously installation roadmap because other steps are needed before to migrate command.

Otherwise, if you have already a Django project built, in a new Terminal window, select the virtual environment again and give the order to build the database, finally:
```
python manage.py makemigrations
python manage.py migrate
```
Or
```
uv run manage.py makemigrations
uv run manage.py migrate
```

---

**CHECK IDE EXTENSIONS FOR THIS DB:**

VSCode: [ide/vscode/\_vscode-knowledge](ide/vscode/_vscode-knowledge.md)

PyCharm: [ide/pycharm/temp](ide/pycharm/temp.txt)
