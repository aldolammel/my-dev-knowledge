#### Python > Project types > Discovery
# Updating Python version in an existing project

---
## Before:

1. [ ] Assuming you have finished Python discovery: [/python/0-new-project/discovery-python](/python/0-new-project/discovery-python.md)
2. [ ] Did you obtain approval for this update/upgrade from the IT product lead/product leader through an official channel?
3. [ ] Assuming you already have done the system backup!
	- [Backup on PostgreSQL](/database/PostgreSQL/backup-on-postgresql.md)
	- [Backup on MariaDB](/database/MariaDB/backup-on-maria.md)
	- [Backup on MySQL](/database/MySQL/backup-on-mysql.md)
	- [Backup on SQLite](/database/SQLite/backup-on-sqlite.md)
	- [Backup on CassandraDB](/database/CassandraDB/backup-on-cassandra.md)
4. [ ] Assuming you already have done the files backup!

---
## 1) Make a choice, which tool are you using:

- 1A) Using UV package manager;
- 1B) Using Python only;- 

................................
### 1A) Using UV

**Before:**
1. [ ] Assuming you already got UV installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

**A.1) Check the current Python versions installed and install that you need:**

- [ ] In your global local environment, check it, and add the new one:
```bash
uv python list
# Adding a new one, e.g.:
uv python install 3.13.9
```

**A.2) In your project folder/environment, set up:**

- [ ] Before: defining to UV which Python version the project must run, e.g.: [/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)

- [ ] A.2.1) (If applicable) In `pyproject.toml` file, update Python version:
```toml
[project]
...
requires-python = "==3.13.9"  # Or ">=3.13.7,<3.14"
```

- [ ] A.2.2) (If applicable) In `pyproject.toml` file, if using [Ruff](/python/linter-formatter-typechecker/ruff/_about.md):
```toml
[tool.ruff]
...
target-version = "py313"  # Python (py313 means newest of 3.13 = 3.13.9) <------
```

- [ ] A.2.3) (If applicable) In `pyproject.toml` file, if using *MyPy*:
```toml
[tool.mypy]
...
python_version = "3.13"  # 3.13 means newest of 3.13 = 3.13.9  <----------------
```

- [ ] A.2.4) Sync the environment (UV will recreate `venv` with new Python): [/python/package-manager/uv/auto-installation-with-sync](/python/package-manager/uv/auto-installation-with-sync.md)

- [ ] A.2.5) Deactivate and active the project environment: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

- [ ] A.2.6) Verify the Python version in the environment:
```bash
uv run python --version
```

**A.3) (Optional) Uninstalling trash:**

 - [ ] Removing unwanted Python versions: [/python/package-manager/uv/uninstall-python-old-version](/python/package-manager/uv/uninstall-python-old-version.md)

......................................
### 1B) Using Python only

**Before:**
1. xxxxx

**B1) xxxxxxxxxxxx**

**B2) xxxxxxxxxxxx**

---
## 2) Once the Python is updated:
Finish this roadmap asking yourself if a Python framework shouldn't be updated/upgraded too: [/python/0-new-project/discovery-python](/python/0-new-project/discovery-python.md)

---
