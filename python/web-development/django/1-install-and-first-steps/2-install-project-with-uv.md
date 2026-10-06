#### Python > Django
# Project installation: using UV as package manager

---

- [x] PRE.1) If you wanna re-install an existing project, skip this roadmap, and go to: [/python/web-development/django/1-install-and-first-steps/3-re-install-project-with-uv](/python/web-development/django/1-install-and-first-steps/3-re-install-project-with-uv.md)

- [x] PRE.2) Assuming you already have UV package manager globally installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---
## Before:
1. [x] DON'T create venv yet!
2. [x] Make sure you already installed all Python versions for this project:

Check which Python versions you got installed:
```bash
uv python list
```
E.g. you want to install more than one Python version:
```bash
uv python install 3.11 3.12 3.13
```
You'll select the right one later!

- [x] **1) (Optional) Advanced IDE configure for Python in this project:**

Python basics:
- For project: `/python/ide/vscode/examples/.vscode/`
- For API only: the same example above!

---
## Project Creation:

### 1) Folder structure

1. [x] Create only the project root folder, e.g. `.../projects/my_new_project/`
2. [x] Just for your information, a Django project further will be like this but don't create anything now: [/python/web-development/django/django-project-folder-structure](/python/web-development/django/django-project-folder-structure.md)
### 2) IDE steps

- [x] 2.1) Select through the IDE GUI which User Profile this project demands!
```
# Aldo's profile backups:
/ide/vscode/user-profiles-bkp/
/ide/pycharm/xxxxxxxxxxxxxxxx/
```

- [x] 2.2) Open this new folder in your IDE;
### 3) (If applicable) Project versioning

- [x] Create a repository or use an existing one: [/versioning/git/command-init](/versioning/git/command-init.md)
### 4) Creating new project with UV

==CRITICAL== 
Never copy a `pyproject.toml` file from other project because it would bring dependencies that this project won't need!

- [x] 4.1) Create the virtual environment folder: [/python/package-manager/uv/create-or-find-current-venv](/python/package-manager/uv/create-or-find-current-venv.md)

- [x] 4.2) (Optional) Create the minimum Python project scaffolding:

==BE AWARE==
The next command can override a few files if you skip steps and put other files in the project root folder!

That said, do it:
```bash
uv init
```

- [x] 4.3) Once UV created a new `pyproject.toml` file, carefully, check this model below and bring the `[project.urls]` and other data to your empty project `.toml` file:

[/python/web-development/pyproject.toml](/python/web-development/pyproject.toml)

- [x] 4.4) Once you now got a `.venv` folder, active the project's virtual environment:

[/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

- [x] 4.5) (Optional) Advanced IDE configure for this framework in this project:

Django basics:
- For project: `.../django/ide/vscode/examples/.vscode/`
- For API only: `.../django/ide/vscode/examples/.vscode-for-api-only/`

Check if the Python version on that file is correct! If NOT okay, fix it: e.g. `requires-python = ">=3.13,<3.14"`

Check the `.python-version` file (if you don't have one, no worries, the command below would create it):
- In case this file has the wrong Python version or versions, don't edit directly this file. Use the pin command: [/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)

- [x] 4.6) Install Django in this project:

Install a specific version (recommended):
```bash
uv add django==5.2.9
```

Or the latest version:
```bash
uv add django
```

- [x] 4.7) Define your database case it SHOULDN'T use *SQLite*:
[/python/web-development/django/3-1-models-database/0-installing-and-adminUser/\_define-the-database](/python/web-development/django/3-1-models-database/0-installing-and-adminUser/_define-the-database.md)

**4.8) After Django installation:**

- [x] 4.8.1) Create the Django Project structure, going to the project root folder and asking the package manager to create the 'core' folder:

```bash
uv run django-admin startproject core .     # This dot's important!
```

==Observation about SQLite file==
Even though you are not using SQLite for this project, this previous step created a SQLite file in your project root folder. Don't worry about it. It will be managed further.

- [x] 4.8.2) Carefully, bring to the new Django Core `settings.py` file those notations you find in this model (don't get concerned with DB stuff yet if this project need a non-SQLite db): [/python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py](/python/web-development/django/z-project-examples/proj-aldolammel-style/core/settings.py)

- [x] 4.8.3) Create the `apps` package folder: [/python/web-development/django/2-creating-and-deleting-apps/apps-package-creation](/python/web-development/django/2-creating-and-deleting-apps/apps-package-creation.md)
      
- [x] 4.8.4) (If applicable) Case you need an admin user:
[/python/web-development/django/3-1-models-database/0-installing-and-adminUser/creating-admin-user](/python/web-development/django/3-1-models-database/0-installing-and-adminUser/creating-admin-user.md)

---
### 5) (Optional) Installing the dependencies
Based on the project's *Technical Design Document (TDD)*, install all dependencies: [/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)

- [x] 5.1) Installing Core dependencies.
- [x] 5.2) Installing Development dependencies.
- [x] 5.3) The *Technical Design Document* URL must be added into the Django `settings.py` file!

---
## 6) (Optional) Multilingual support:
- [x] **Before:** [Gettext](/python/component-libraries/gettext/0-gettext.md) installed.
- [x] Run both commands:
```bash
uv run manage.py makemessages --all
uv run manage.py compilemessages
```

---
## 7) (If applicable) .gitignore configure:
- [x] Make sure you got the project `.gitignore` updated with Django, environment and other things: [/versioning/git/gitignore-file](/versioning/git/gitignore-file.md)

---
## 8) Django tests:
- [x] Check Django installation and setup: [/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---

==Since this point, you might execute basic tests without the follow steps once your goal would be to test something basic on Django.==

---

- [x] 9) (If applicable) Commit files in your versioning service (e.g. GitHub)!

- [ ] 10) Let's setup the new project: [/python/web-development/django/1-install-and-first-steps/2.2-installed-project-setup](/python/web-development/django/1-install-and-first-steps/2.2-installed-project-setup.md)

---
## MAKE SURE YOU FINISHED ALL THESE STEPS:
[/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup](/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup.md)
