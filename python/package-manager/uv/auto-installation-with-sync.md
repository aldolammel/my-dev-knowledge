#### Python > Package Manager > UV

# Using sync command

The command looks for project files that listing the configurations and dependencies (like _pyproject.toml_, _requirements.txt_). Once UV read, for example, the _pyproject.toml_ file, it automatically updates _uv.lock_ file! UV makes it comparing the desired state (your project files) with the current state (what's already installed) and calculates the difference. The most import file for _uv sync_ is _uv.lock_ (in project folder root) that is dynamically managed.

**Only in case of _requirements.txt:_**

Convert your current existing project using _requirements.txt_ to use _pyproject.toml_ file: [[converting-non-uv-project-in-one]]

---

## 1) Make a choice:

- 1A) I'm updating Python in a project;
- 1B) I lost the virtual environment folder in a project;
- 1C) I just cloned an existing project repo;
- 1D) Something wrong with my project dependencies;

### 1A) I'm updating Python in a project

In your project folder/environment, it deletes the current .venv folder and recreate it:

**Before:**

1. Assuming you are in the project environment!
2. Assuming you already pin the new Python version through _UV_ (like you should have updated the _.python-version_ file): [[pin-python-version]]
3. Assuming the Python version's manually updated in the _pyproject.toml_ file! (/python/web-development/pyproject.toml)

**A1.1) Syncing, make a choice**:

Option 1: Mandatory ones and all dependencies from development sub-group:

```
uv sync --extra dev
```

Option 2: Only the mandatory dependencies:

```
uv sync
```

Option 3: Mandatory ones, including multiples sub-groups of dependencies:

```
uv sync --extra dev --extra test
```

### 1B) I lost the virtual environment folder in a project

In your project folder/environment, recreate the venv folder, using one of those options in 'Syncing' (A1.1) step above!

### 1C) I just cloned an existing project repo

In your project folder/environment, recreate the venv folder, using one of those options in 'Syncing' (A1.1) step above!

### 1D) Something wrong with my project dependencies

In your project folder/environment, reinstall dependencies, using one of those options in 'Syncing' (A1.1) step above!

---
