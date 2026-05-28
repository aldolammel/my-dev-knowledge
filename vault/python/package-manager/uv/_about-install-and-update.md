#### Python > Package Manager

# UV

Extremely fast Python package installer and resolver designed as a drop-in replacement for pip and pip-tools workflows. Official docs: https://docs.astral.sh/uv/getting-started/installation/

When you ask to UV to initiate a project, a _uv.lock_ file is created automatically, guaranteeing that all copies of this project will have the same dependencies (like a _Docker_);

---

## 1) Installing:

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

```
winget install --id=astral-sh.uv  -e
```

**1.2) Restart your terminal to include definitely UV stuff in the local machine $PATH!**

**1.3) Test it:**

```
uv --version
```

**1.4) (If applicable) If needed, update it:** [[upgrade-uv]]

---

## 2) Using UV:

**Before:**

1. Create / Recreate (or find the current) venv in your project folder: [[create-or-find-current-venv]]

**Create the minimal Python project scaffolding:**
It creates automatically some files like _pyproject.toml_. Don't use this for existing projects with these files already!

```
uv init
```

**Updating or restoring Python, and project dependencies (existing projects ongoing):**

[[auto-installation-with-sync]]

**Install package (only in the active virtual environment):**

[[install-dependency]]

**Check installed dependencies:**

```
uv pip list
```

**Uninstall package (only in the active virtual environment):**

[[uninstall-dependency]]

---

**DJANGO PROJECT WITH UV:**

/vault/python/web-development/django/1-install-and-first-steps/2-install-project-with-uv.txt

**FLASK PROJECT WITH UV:**

/vault/python/web-development/flask/1-install-and-first-steps/2-install-project-with-uv.txt

**HOW TO CREATE A REQUIREMENTS OF PROJECT WITH UV:**

[[creating-requirements-of-project]]
