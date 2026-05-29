#### Python > Package Manager > UV

# Creating requirements of a project

Install requirements with UV is much more powerful and manageable than _requirements.txt_ file that is important to get to know some concepts and what is the _pyproject.toml_ file:

---

## Before:

1. Assuming you already installed UV: [[_about-install-and-update]]
2. What dependencies are (below);

**What dependencies are:**

They are packages required in order to run an app in any environment, no matter if it's production, staging or development one.

**What optional-dependencies are:**

They are packages NOT required to run an app, but they make tasks easier:

- **Sub-group _dev_:** Contains everything needed for development: testing frameworks, linters, formatters, debuggers, doc builders, etc.
- **Sub-group _test_:** Often a subset of dev focused purely on testing.
- **Sub-group _docs_:** Tools for building documentation.

The file _pyproject.toml_ (PEP 621) manages all dependencies (including the optional ones) of a specific project:

E.g. /vault/python/web-development/pyproject.toml

---

## 1) Make a choice:

- 1A) I am the new developer in an existent project;
- 1B) Or I am building a new project;
- 1C) Or someone ask me for the _requirements.txt_ file from the project I'm working on;

### 1A) I am the new developer in an existing project

A.1) After you clone the project's repo, the pyproject.toml should be in the project's root;

A.2) Once you are in the project's folder, create the virtual environment for it BUT NEVER use the _uv init_ in this case 'coz it would replace important files like the _pyproject.toml_. You also shouldn't use the _uv venv_ command eather!

==Info!==
The next step using 'sync' already will create the environment!

A.3) Make sure the the pyproject.toml file in on the project's root, so then install the project requirements, creating also the virtual environment for them:
[[auto-installation-with-sync]]

### 1B) I am building a new project

**B.1) Once in the project root:**
Ask UV to create the virtual environment folder: [[python/package-manager/uv/create-or-find-current-venv]]

**B.2) Ask UV to install the minimal Python project scaffolding files:**

==Attention!==
If you wanna use existing _pyproject.toml_ and _.gitignore_ files for example, be aware once the _init_ command will create those files with others, overriden files in project folder is not empty!

That said, do it:

```
uv init
```

**B.3) To add new packages with UV:**

Mandatory package:

```
uv add <package_name>
```

Optional package for dev:

```
uv add --optional <sub-group> <package_name>
```

E.g.

```
uv add --optional dev ruff
```

### 1C) Someone ask me for the _requirements.txt_ file from the project I'm working on

Ask them to clone the project's repository if (recommended) the _pyproject.toml_ is there!

---

**HOW TO ADD NEW PACKAGES WITH UV:**
[[python/package-manager/uv/install-dependency]]

**HOW TO REMOVE PACKAGES WITH UV:**
[[uninstall-dependency]]
