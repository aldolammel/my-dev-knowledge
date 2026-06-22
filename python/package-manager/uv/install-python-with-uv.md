#### Python > Package Manager > UV
# Installing Python with UV

---
## 1) Installing:

**Before:**
1. Assuming you already set up your UV: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

**Make a choice:**
- 1A) Using UV, install Python by project (RECOMMENDED);
- 1B) Or using UV too, but install Python globally;
### 1A) Using UV, install Python by project
Most professional and long-term approach, once it's easier to update Python in case the VPS would gain new apps in parallel, for example.

**Before:**
1. Assuming you're activated in the right app venv: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md);
2. (If applicable) Make sure your *pyproject.toml* file has the right Python version declared, otherwise it will prevent a different Python version installation.

**1A.1) Install it by project:**
```
uv venv --python <python-version>
```
E.g.
```
uv venv --python 3.13.5
```
1A.2) Check the version installed:
```
uv run python --version
```
1A.3) (If applicable) Make sure the right Python version is already pinned in the project's .python-version file:
```
nano .python-version
```
If not, fix it doing this: [/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)
### 1B) Or using UV too, but install Python globally
This approach will install Python outside any project. For single-purpose servers, it could be an option but can be risky in long-term.

**Before:**
1. Assuming you're NOT in a project virtual environment!

**1B.1) Install it globally:**
```
uv python install <python_version>
```
E.g.
```
uv python install 3.13.5
```

---
## Uninstalling Python version with UV:
[/python/package-manager/uv/uninstall-python-old-version](/python/package-manager/uv/uninstall-python-old-version.md)
## Install Python dependencies:
[/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)
## Uninstall Python dependencies:
[/python/package-manager/uv/uninstall-dependency](/python/package-manager/uv/uninstall-dependency.md)
