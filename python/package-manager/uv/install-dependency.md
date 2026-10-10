#### Python > Package Manager > UV
# Installing a dependency (`uv add` command)

---

Once this command is used to add a new dependency, automatically UV includes the dependency in the [pyproject.toml](python/pyproject-toml.md) dependency list and execute the [uv sync command](/python/package-manager/uv/uv-sync.md) behind the scene, updating also the [uv.lock](/python/package-manager/uv/uv-lock.md) file and the `.venv` folder.

---
## Before:

1. What is [UV](/python/package-manager/uv/_about-install-and-update.md).
2. Avoid to use `uv pip install <package_name>` once this command doesn't automatically update crucial files in a project like `uv.lock` and `pyproject.toml`.

---
## 1) Using the command:

**Make a choice:**
- 1A) I wanna install a dependency and my project has a `pyproject.toml`.
- 1B) I wanna install a dependency and my project has a `requirements.txt`.
- 1C) I wanna install a dependency free of any requirements file.

......................................
### 1A) I wanna install a dependency and my project has a `pyproject.toml`

Installing an app-level core dependency:
```bash
uv add <package_name>
# E.g. $ uv add django
```
Installing an app-level non-core dependency:
```bash
uv add --group <sub-group> <package_name>
# E.g. $ uv add --group dev ruff
```

......................................

### 1B) I wanna install a dependency and my project has a `requirements.txt`

1B.1) Installing a dependency (no matter if core or not):
```bash
uv pip install <package_name>
# E.g. $ uv pip install django
```

1B.2) After that, include this dependency in the right file:
- [requirements.txt](/python/requirements-txt.md)
- [requirements-dev.txt](/python/requirements-dev-txt.md)
- [requirements-prod.txt](/python/requirements-prod-txt.md)

......................................

### 1C) I wanna install a dependency free of any requirements file:
Make exactly the same thing of the 1B but without to include the dependency anywhere.

---
## 2) Checking what you've installed:
```bash
uv pip list
```

---
## Update dependencies with UV:
[/python/package-manager/uv/upgrade-dependencies](/python/package-manager/uv/upgrade-dependencies.md)
## Uninstall dependency with UV:
[/python/package-manager/uv/uninstall-dependency](/python/package-manager/uv/uninstall-dependency.md)
## Install Python version with UV:
[/python/package-manager/uv/install-python-with-uv](/python/package-manager/uv/install-python-with-uv.md)
## Uninstall Python version with UV:
[/python/package-manager/uv/uninstall-python-old-version](/python/package-manager/uv/uninstall-python-old-version.md)
