#### Python > Package Manager > UV
# Uninstalling dependencies (`uv remove` command)

---

Once this command is used to remove a dependency, automatically UV deletes the dependency from the [pyproject.toml](python/pyproject-toml.md) dependency list and execute the `uv sync` behind the scene, updating the [uv.lock](/python/package-manager/uv/uv-lock.md) file and the `.venv` folder.

---
## Before:
1. What is it: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---
## 1) Removing a dependency from everywhere, regardless it's core or not:
```bash
uv remove <package_name>
```
Remove the dependency from a specific group:
```bash
uv remove --group <sub-group> <package_name>
# E.g. uv remove --group dev ruff
```

---
## INSTALL DEPENDENCY:
[/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)
## UPDATE DEPENDENCY:
[/python/package-manager/uv/upgrade-dependencies](/python/package-manager/uv/upgrade-dependencies.md)
