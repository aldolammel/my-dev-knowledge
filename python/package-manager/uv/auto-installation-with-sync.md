#### Python > Package Manager > UV
# Using sync command

---

==Critical / On Prod:==
Read this in case you wanna do it on production environment: [/python/package-manager/uv/production-with-uv](/python/package-manager/uv/production-with-uv.md)

---

The `uv sync` command looks for project `pyproject.toml` file to listing the configurations and dependencies and, if something changed in the `pyproject.toml`, the command will update the `uv.lock` file and the `.venv` folder.

**Command scope:**
- `uv.lock` is the central file, and uv manages it, so you shouldn't edit `uv.lock` by hand.
- It does re-lock automatically if `pyproject.toml` changed (for example, you added or edited a dependency).
- It compares the lock-file against what's in your `.venv` and installs, removes or changes only what differs. By default the sync is exact, so packages not in the lock get removed.

**Only in case of `requirements.txt`:** 
- Convert your current existing project using `requirements.txt` to use `pyproject.toml` file: [/python/package-manager/uv/converting-non-uv-project-in-one](/python/package-manager/uv/converting-non-uv-project-in-one.md)

---
## 1) Make a choice:

- 1A) I'm updating Python in a project.
- 1B) I'm updating `pyproject.toml` dependency version limitations.
- 1C) I lost the virtual environment folder in a project.
- 1D) I just cloned an existing project repo.
- 1E) Something wrong with my project dependencies.

......................................
### 1A) I'm updating Python in a project

In your project folder/environment, it deletes the current `.venv` folder and recreate it:

- [ ] **Before:**

1. Assuming you are in the project environment!
2. Assuming you manually pinned the new Python version through UV (like you should have updated the `.python-version` file): [/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)
3. Assuming you manually updated the Python version in the `pyproject.toml`.

- [ ] **A1.1) Syncing, make a choice**:

Option 1: Mandatory ones and all dependencies from development sub-group:
```bash
uv sync --extra dev
```

Option 2: Only the mandatory dependencies:
```bash
uv sync
```

Option 3: Mandatory ones, including multiples sub-groups of dependencies:
```bash
uv sync --extra dev --extra test
```

- [ ] **A1.2) Make sure `uv.lock` is synced with what `pyproject.toml` is saying:**
```bash
uv lock --check  # Optional 'cuz, after the sync command, it's almost impossible any issue in 'uv.lock' file.
uv run python --version
```

......................................
### 1B) I'm updating `pyproject.toml` dependency version limitations

Case you went to that file and updated one or more dependency version, you need to re-sync for make the uv.lock file and the .venv folder get updated if needed. So, in your project folder/environment, do the A1 steps!

......................................
### 1C) I lost the virtual environment folder in a project

In this case you need to re-create the `.venv` folder based in what your `pyproject.toml` file is describing. So, in your project folder/environment, do the A1 steps!

......................................
### 1D) I just cloned an existing project repo

Once you have no any `.venv` created for this project yet (at least it should be available in a repository), in your project folder/environment, do the A1 steps!

......................................
### 1E) Something wrong with my project dependencies

In this scenario, the first thing to know is if you still have the pyproject.toml file in your project root folder. If not, you should read about [uv init](/python/package-manager/uv/install-python-with-uv.md). If you 
In your project folder/environment, reinstall dependencies, using the A1 steps!

---


