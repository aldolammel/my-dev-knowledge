#### Python > Django
# Project installation: using UV as package manager

---

- [ ] PRE) If you wanna re-install an existing project, skip this roadmap, and go to: [/python/web-development/django/1-install-and-first-steps/3-re-install-project-with-uv](/python/web-development/django/1-install-and-first-steps/3-re-install-project-with-uv.md)

---
## Before:

1. [ ] Assuming you already have UV package manager globally installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)
2. [ ] DON'T create `.venv` yet!
3. [ ] Make sure you already installed all Python versions for this project:

Check which Python versions you got installed:
```bash
uv python list
```
E.g. you want to install more than one Python version:
```bash
uv python install 3.11 3.12 3.13
```
You'll select the right one later!

- [ ] **1) (Optional) Advanced IDE configure for Python in this project:**

Python basics:
- For project: `/python/ide/vscode/examples/.vscode/`
- For API only: the same example above!

---
## Project Creation:

### 1) Folder structure

1. [ ] Create only the project root folder, e.g. `/projects/my_new_django_project/`
2. [ ] Just for your information, a Django project further will be like this but don't create manually anything for now: [/python/web-development/django/django-project-folder-structure](/python/web-development/django/django-project-folder-structure.md)
### 2) IDE steps

- [ ] 2.1) Select through the IDE GUI which User Profile this project demands!
```
# Aldo's profile backups:
/ide/vscode/user-profiles-bkp/
/ide/pycharm/xxxxxxxxxxxxxxxx/
```

- [ ] 2.2) Open this new project folder in your IDE;
### 3) (If applicable) Project versioning

- [ ] Create a repository or use an existing one: [/versioning/git/command-init](/versioning/git/command-init.md)
### 4) Creating new project with UV

==CRITICAL== 
Never copy a `pyproject.toml` or `requirements.txt` file from other project because it would bring dependencies that this project won't need!

- [ ] 4.1) Create the virtual environment folder: [/python/package-manager/uv/create-or-recreate-venv](/python/package-manager/uv/create-or-recreate-venv.md)

- [ ] 4.2) (Optional) Create the minimum Python project scaffolding: [/python/package-manager/uv/uv-init](/python/package-manager/uv/uv-init.md)

- [ ] 4.3) Once UV has been created a new `pyproject.toml` file, carefully bring the `[project.urls]` and those notes/comments from the `.toml` model: [pyproject.toml](/python/pyproject-toml.md).

- [ ] 4.4) Once you got a `.venv` folder, active the project's virtual environment: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

- [ ] 4.5) Check the `.python-version` file (if you don't have one, no worries, the command below would create it):
- In case this file has the wrong Python version, don't edit the file directly. Use the `uv pin` command: [/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)

- [ ] 4.6) (Optional) Advanced IDE configure for this framework:
	- Django basics:
		- For project: `.../django/ide/vscode/examples/.vscode/`
		- For API only: `.../django/ide/vscode/examples/.vscode-for-api-only/`

- [ ] 4.7) Install Django in this project:

Install a specific version (recommended):
```bash
uv add django==5.2.9
```
Or the latest version:
```bash
uv add django
```

- [ ] 4.8) Define your database case it SHOULDN'T use *SQLite*:
[/python/web-development/django/3-1-models-database/0-installing-and-adminUser/\_define-the-database](/python/web-development/django/3-1-models-database/0-installing-and-adminUser/_define-the-database.md)

**4.9) After Django installation:**

- [ ] 4.9.1) Create the Django core folder, going to the project's root folder and:
```bash
uv run django-admin startproject core .     # This dot is important!
```

==Observation about SQLite file==
Even though you are not using SQLite for this project, this previous step created a SQLite file in your project root folder. Don't worry about it. It will be managed further.

- [ ] 4.9.2) Carefully, bring to the new Django `/core/settings.py`  those notes you'll find in this next model (don't get concerned with DB stuff yet if this project need a non-SQLite db): [/python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py)

- [ ] 4.9.3) (Optional) For your `core` folder, bring from these files below the main notes/comments that can help you for future use:
	- /core/[consts.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/consts.py)
	- /core/[models.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/models.py) (E.g. to store AuditMixin model class)
	- /core/[lang.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/lang.py)

- [ ] 4.9.4) Create the `apps` package folder: [/python/web-development/django/2-creating-and-deleting-apps/apps-package-creation](/python/web-development/django/2-creating-and-deleting-apps/apps-package-creation.md)

- [ ] 4.9.5) (Optional) For each `/apps/subapp/`, bring from these files below the main notes/comments that can help you for future use:
	- /apps/subapp_name/[consts.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/consts.py)
	- /apps/subapp_name/[models.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/models.py)
	- /apps/subapp_name/[admin.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/admin.py)
	- /apps/subapp_name/[validators.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/validators.py)
	- /apps/subapp_name/[forms.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/forms.py)
	- /apps/subapp_name/[utils.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/utils.py)
	- /apps/subapp_name/[serializers.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/apps/sub_app_1/serializers.py) (If applicable: demands a REST module)
	- /apps/subapp_name/[lang.py](/)

- [ ] 4.9.6) (If applicable) Case you need an admin user:
[/python/web-development/django/3-1-models-database/0-installing-and-adminUser/creating-admin-user](/python/web-development/django/3-1-models-database/0-installing-and-adminUser/creating-admin-user.md)
### 5) (Optional) Installing the dependencies
Based on the project's *Technical Design Document* (TDD), install all dependencies: [/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)

- [ ] 5.1) Installing Core dependencies.
- [ ] 5.2) Installing Development and Production dependencies.
- [ ] 5.3) The *Technical Design Document* URL must be added into the Django `settings.py` file!
### 6) (Optional) Multilingual support
- [ ] **Before:** [Gettext](web-development/components-libraries-server-level/gettext/0-gettext.md) installed.
- [ ] Run both commands:
```bash
uv run manage.py makemessages --all
uv run manage.py compilemessages
```
### 7) (If applicable) `.gitignore` configure
- [ ] Make sure you got the project `.gitignore` updated with Django, environment and other things: [/versioning/git/gitignore-file](/versioning/git/gitignore-file.md)
### 8) Django tests
- [ ] Check Django installation and setup: [/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---

==Since this point, you might execute basic tests without the follow steps once your goal would be to test something basic on Django.==

---
### 9) (If applicable) Time to save a copy of your initial app:
- [ ] Commit files in your versioning service (e.g. GitHub)!
### 10) Setup the new application:
- [ ] Let's setup the new project: [/python/web-development/django/1-install-and-first-steps/2.2-installed-project-setup](/python/web-development/django/1-install-and-first-steps/2.2-installed-project-setup.md)

---
## Once you are here, make sure you have finished all this steps:
[/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup](/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup.md)
