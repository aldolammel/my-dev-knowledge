#### Python > Package Manager > UV
# Creating requirements of a project

---

The `pyproject.toml` file (PEP 621) manages all dependencies of a specific project, e.g., [/python/pyproject-toml](/python/pyproject-toml.md). Install requirements with UV is much more powerful and manageable than [requirements.txt](/python/requirements-txt.md) file that is important to get to know some concepts and what is the `pyproject.toml` file.

---
## Before:

1. Assuming you already installed UV: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)
2. What dependencies are (below);
### What core-dependencies are
They are packages required in order to run an app in any environment, no matter if it's [Prod](/dev-concepts/environment-production-prod.md), [UAT](/dev-concepts/environment-staging-uat.md), [Dev](/dev-concepts/environment-development-dev.md) or [QA](/dev-concepts/environment-testing-qa.md) one.
### What NON-core-dependencies are
They are packages NOT required to run the app in a few circumstances:

- **Group _dev_:** Contains everything needed for [development](/dev-concepts/environment-development-dev.md) and [QA](/dev-concepts/environment-testing-qa.md) environments: testing frameworks, linters, formatters, debuggers, doc builders, etc.
- **Group _test_:** Often a subset of dev focused purely on testing.
- **Group _prod_:** Contains everything needed to run the app on [production](/dev-concepts/environment-production-prod.md) and [UAT](/dev-concepts/environment-staging-uat.md) environments: app servers (e.g. gunicorn), error tracking (e.g. sentry-sdk), and prod-only integrations.
- **Group _docs_:** Tools for building documentation.

---
## 1) Make a choice:

- 1A) I am the new developer in an existent project.
- 1B) I am building a new project from scratch.
- 1C) Someone ask me for the [requirements.txt](/python/requirements-txt.md) file from the project I'm working on;

......................................

### 1A) I am the new developer in an existing project

A.1) After you clone the project's repo, the `pyproject.toml` should be in the project's root.

A.2) Once you are in the project's folder, create the virtual environment for it BUT NEVER use the `uv init`, otherwise this command could override your requirements file. You also shouldn't use the `uv venv` command either because the next command will do it automatically!

A.3) Create the `.venv` folder and install all core and dev dependencies in a row: [/python/package-manager/uv/auto-installation-with-sync](/python/package-manager/uv/auto-installation-with-sync.md)

......................................

### 1B) I am building a new project from scratch

B.1) Once in the project root, ask UV to create a brand new `.venv`: [/python/package-manager/uv/create-or-recreate-venv](/python/package-manager/uv/create-or-recreate-venv.md)

B.2) Ask UV to install the minimal Python project scaffolding files: [/python/package-manager/uv/uv-init](/python/package-manager/uv/uv-init.md)

B.3) Based on your *Technical Design Document* (TDD), add all app-level dependencies with UV:

**Core dependencies:**
```bash
uv add <package_name>
```

**Non-core dependencies:**
For dev dependencies:
```bash
uv add --group dev <package_name>
```
For prod dependencies:
```bash
uv add --group prod <package_name>
```

......................................

### 1C) Someone ask me for the `requirements.txt` file from the project I'm working on
Ask them to clone the project's repository if (recommended) the `pyproject.toml` is there!

---

**HOW TO ADD NEW PACKAGES WITH UV:**
[[/python/package-manager/uv/install-dependency]]

**HOW TO REMOVE PACKAGES WITH UV:**
[[uninstall-dependency]]
