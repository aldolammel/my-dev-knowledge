#### Python > Package Manager > UV
# Uninstalling dependencies (`uv remove` command)

---

Once this command is used to remove a dependency, automatically UV deletes the dependency from the [pyproject.toml](python/pyproject-toml.md) dependency list and execute the `uv sync` behind the scene, updating the [uv.lock](/python/package-manager/uv/uv-lock.md) file and the `.venv` folder.

---
## Before:
1. What is it: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---
## 1) Removing a dependency:

If core-dependency:
```bash
uv remove package_name_here
```

If dev or other group of dependency:
```bash
uv remove --group sub_group_here package_name_here
# E.g. uv remove --group dev ruff
```

---
## 2) (If applicable) Installed apps:
Make this dependency is not installed in `/core/settings.py` file.

---
## Install dependency:
[/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)
## Update dependency:
[/python/package-manager/uv/upgrade-dependencies](/python/package-manager/uv/upgrade-dependencies.md)



