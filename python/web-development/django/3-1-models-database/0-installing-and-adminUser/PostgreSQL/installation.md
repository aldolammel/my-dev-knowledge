#### Python > Django > Installing
# Using PostgreSQL

---

**Summary:**
1) Installing the db with its basic integration;
2) Integrating database and back-end;
3) Creating the database;

---
## 1) Installing the db with its basic integration

- [x] If the db won't be in the cloud, install it locally: [/database/PostgreSQL/0-basic/1-installing-and-integrating](/database/PostgreSQL/0-basic/1-installing-and-integrating.md)

---
## 2) Integrating database and back-end

**Before:**
1. [x] Django already installed.
2. [x] You already have created a database for the project.
3. [x] You already ran the `django-admin startproject` command!

- [x] **2.1) Make a copy of the `.env` file to your project root folder:**  [/environment-variables/env-for-local/in-backend/.env](/environment-variables/env-for-local/in-backend/.env)

- [x] 2.2) Configure the `.env` with the PostgreSQL database created for the project;
	- DATABASE_NAME
	- DATABASE_USER
	- DATABASE_PASSWORD
	- ...

- [x] **2.3) Install the dependency responsible for *Environment Variables* for this project:** Check the *Technical Design Document* for this project, and install ONLY the module for environ var management for now: [/python/web-development/django/Env-Var-Managers/\_options](/python/web-development/django/Env-Var-Managers/_options.md)

- [x] **2.4) Install a Python lib for PostgreSQL:**  [/python/component-libraries/psycopg/0-psycopg](/python/component-libraries/psycopg/0-psycopg.md)

- [x] **2.5) Through `settings.py`, tell to Django to use PostgreSQL:** 
```
# Make sure you have this somewhere in your settings.py:
DB_CONN_TIMEOUT = 600
if DEBUG:
	DB_CONN_TIMEOUT = 0

# On local:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DATABASE_NAME"),
        "USER": env("DATABASE_USER"),
        "PASSWORD": env("DATABASE_PASSWORD"),
        "HOST": env("DATABASE_HOST"),
        "PORT": env("DATABASE_PORT"),
        "CONN_MAX_AGE": DB_CONN_TIMEOUT,
        "CONN_HEALTH_CHECKS": True,  # Ensure the connection's still alive before reusing it.
    }
}
```

If something wrong, check my `settings.py` model: [/python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py)

- [x] **2.6) Delete the sqlite.db:** If you see the file in the project root folder, delete it once you are using PostgreSQL and you have no data from this project in that SQLite.

---
## 3) Creating the db

==Attention!==
If you are installing a new Django project, return to the previously installation roadmap because other steps are needed before to migrate command.

Otherwise, if you have already a Django project built, in a new Terminal window, select the virtual environment again and give the order to build the database, finally:

Using UV:
```
uv run manage.py makemigrations
uv run manage.py migrate
```
Or using Python solution:
```
python manage.py makemigrations
python manage.py migrate
```

- [x] So I already created the project db!

---

## Check IDE extensions for this DB:
- VSCode: [/ide/vscode/\_vscode-knowledge](/ide/vscode/_vscode-knowledge.md)
- PyCharm: [/ide/pycharm/temp](/ide/pycharm/temp.txt)
