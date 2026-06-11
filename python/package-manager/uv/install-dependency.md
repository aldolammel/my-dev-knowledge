#### Python > Package Manager > UV
# Installing Dependencies

---
## Before:
1. What is it:  [[_about-install-and-update]] 
2. Avoid to use *uv pip install <package_name>* once this command doesn't automatically update crucial files in a project like *uv.lock* and *pyproject.toml*.

---
## 1) Installing dependencies:

**Make a choice:**
- 1A) Installing dependencies when the project has a pyproject.toml or similar;
- 1B) Installing dependencies freely.****
### 1A) Installing dependencies when the project has a pyproject.toml or similar

Installing mandatory dependency:
```
uv add <package_name>
```
Installing optional dependency:
```
uv add --optional <sub-group> <package_name>
```
E.g.
```
uv add --optional dev ruff
```
Checking installed ones:
```
uv pip list
```
### 1B) Installing dependencies freely:

Installing dependency:
```
uv pip install <package_name>
```
Checking installed ones:
```
uv pip list
```

---
## Update dependencies with UV:
[python/package-manager/uv/upgrade-dependencies](python/package-manager/uv/upgrade-dependencies.md)
## Uninstall dependency with UV:
[python/package-manager/uv/uninstall-dependency](python/package-manager/uv/uninstall-dependency.md)
## Install Python version with UV:
[python/package-manager/uv/install-python-with-uv](python/package-manager/uv/install-python-with-uv.md)
## Uninstall Python version with UV:
[python/package-manager/uv/uninstall-python-old-version](python/package-manager/uv/uninstall-python-old-version.md)
