#### Python > Django
# Project re-installation: using UV as package manager

---
## Before:

1. If you wanna install a totally new brand project, skip this roadmap, and go to: [/python/web-development/django/1-install-and-first-steps/2-install-project-with-uv](/python/web-development/django/1-install-and-first-steps/2-install-project-with-uv.md)
2. Assuming you already have `uv` package manager globally installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---
## 1) Preparing the project re-installation:

**Before:**
- [ ] Case you have an older and non-function project version in your machine, don't delete that project folder! You may need that further!

**1.1) Locally, create the existing project folder:**
- [ ] Create the folder and get in it: 
	- `$ mkdir <project_folder_v2>`
	- `$ cd <project_folder_v2>`

**1.2) IDE steps:**
- [ ] Open this new folder/project through the IDE;
- [ ] Through the IDE GUI, select which *User Profile* this project demands;

**1.3) Make sure you already installed all Python versions for this project:**
- [ ] Check which Python versions you got installed:
	- `$ uv python list`
- [ ] (If applicable) To install more than one Python version:
	- `$ uv python install 3.11 3.12 3.13`

---
## 2) Project re-creation:

**2.1) Clone the project into the new project folder:**
- [ ] Clone it: [/versioning/git/command-clone](/versioning/git/command-clone.md)

**2.2) (If applicable) Local project folder structure:
- [ ] Don't create any additional folders beyond the project folder you already created, but mentally define which Django folder structure you will use further (use the django structure example only for consulting best practices): [/python/web-development/django/django-project-folder-structure](/python/web-development/django/django-project-folder-structure.md)

**2.3) Create the .venv folder:**
- [ ] UV auto install and sync: [/python/package-manager/uv/auto-installation-with-sync](/python/package-manager/uv/auto-installation-with-sync.md)
- [ ] Make sure you activated the environment: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

**2.4) Installing all project dependencies based on requirements:**
- [ ] Make a decision:
	- Using `pyproject.toml`: nothing to do! `Uv` already synced dependencies when `.venv` folder was created!
	- Or Using `requirements.toml`: [/python/package-manager/pip/auto-installation-from-requirements-file](/python/package-manager/pip/auto-installation-from-requirements-file.md)

**2.5) Choosing the way to create the project's db:**
- [ ] Make a decision:
	- You don't have a local db created yet: [/database/00-new-project/create-db-for-existing-project](/database/00-new-project/create-db-for-existing-project.md)
	- Or you already have the local db created:
		- `$ uv run manage.py makemigrations`
		- `$ uv run manage.py migrate`

**2.6) (If applicable) You got multilingual support in your project:**
- [ ] With `Gettext` module installed:
	- `$ uv run manage.py makemessages --all`
	- `$ uv run manage.py compilemessages`

**2.7) (If applicable) Make sure you got your `.gitignore` updated:**
- [ ] With Django, environment and other things: [/versioning/git/gitignore-file](/versioning/git/gitignore-file.md)

**2.8) Test it:**
- [ ] Check Django installation and setup: [/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing](/python/web-development/django/1-install-and-first-steps/2.1-installed-project-testing.md)

---
## Make sure you finished all these steps:
[/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup](/python/web-development/django/1-install-and-first-steps/0-django-installation-and-setup.md)
