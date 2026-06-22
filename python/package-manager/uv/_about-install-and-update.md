#### Python > Package Manager
# UV

---

Extremely fast Python package installer and resolver designed as a drop-in replacement for pip and pip-tools workflows. Official docs: https://docs.astral.sh/uv/getting-started/installation/

When you ask to UV to initiate a project, a _uv.lock_ file is created automatically, guaranteeing that all copies of this project will have the same dependencies (like a _Docker_).

---
## 1) Installing:

**Before:**
1. Assuming you are activated in a project venv;
2. Check if you already got UV in your machine: $ uv --version
	1. If you got, skip the entire 1 step and its sub-steps and [update UV if needed](/python/package-manager/uv/upgrade-uv.md), going to step 2 next.

**1.1) Choose the OS and install it:**

**Linux/Mac:**
Downloading using _wget_ (bundled on _Debian_ distros):
```
wget -qO- https://astral.sh/uv/install.sh | sh
```
Or downloading using CURL:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows:**
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
And:
```
winget install --id=astral-sh.uv  -e
```

**1.2) Restart your terminal to include definitely UV stuff in the local machine $PATH!**

**1.3) Test it:**
```
uv --version
```

**1.4) (If applicable) If needed, update it:** [/python/package-manager/uv/upgrade-uv](/python/package-manager/uv/upgrade-uv.md)

---
## 2) Using UV:

**Make a choice:**
- 2A) You are starting a new project from scratch;
- 2B) Your project already has development or production files;
### 2A) You are starting a new project from scratch

**Make one more choice:**
- 2A.1A) Create a project with pyproject.toml dependencies and tools control;
- 2A.1B) I just need the venv and nothing else;

**2A.1A) Create a project with *pyproject.toml* dependencies and tools control, and *Git* repository-ready:**

Create the minimal Python project scaffolding. It creates automatically some files like _pyproject.toml_. Don't use this for existing projects with these files already:
```
uv init
```
And then create the venv:
```
uv venv
```

**2A.1B) I just need the venv and nothing else:**
```
uv venv
```

### 2B) Your project already has development or production files

**2B.1) Create or recreate (or even find the current) venv in the project folder:** 

[/python/package-manager/uv/create-or-find-current-venv](/python/package-manager/uv/create-or-find-current-venv.md)

**2B.2) (If applicable) Updating or restoring Python, and project dependencies (existing projects ongoing):**

[/python/package-manager/uv/auto-installation-with-sync](/python/package-manager/uv/auto-installation-with-sync.md)

---
## Install Python version with UV:
[/python/package-manager/uv/install-python-with-uv](/python/package-manager/uv/install-python-with-uv.md)
## Uninstall Python version with UV:
[/python/package-manager/uv/uninstall-python-old-version](/python/package-manager/uv/uninstall-python-old-version.md)
## Install Python dependencies with UV:
[/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)
## Uninstall Python dependencies with UV:
[/python/package-manager/uv/uninstall-dependency](/python/package-manager/uv/uninstall-dependency.md)
## Django project with UV:
[/python/web-development/django/1-install-and-first-steps/2-install-project-with-uv](/python/web-development/django/1-install-and-first-steps/2-install-project-with-uv.md)
## Flask project with UV:
[/python/web-development/flask/1-install-and-first-steps/2-install-project-with-uv](/python/web-development/flask/1-install-and-first-steps/2-install-project-with-uv.md)
## Creating a requirements file of the project with UV:
[/python/package-manager/uv/creating-requirements-of-project](/python/package-manager/uv/creating-requirements-of-project.md)