#### Python > Package Manager > UV

# Creating/Recreating a venv

---
## Before:

1. Assuming you already installed UV: [/python/package-manager/uv/_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)
2. Assuming you're in the project folder.
3. ==Critical:== Don't use `uv init` case you already have `pyproject.toml` and `uv.lock` files.

---
## 1) Create/Recreate it:

**Before:**
- If you don't trust in your current `.venv` folder and this project has a `pyproject.toml` file, you should rename this `.venv` to `.venv_bkp_<todaydate>` to delete it further once the new `.venv` is tested.

UV will create a clean `.venv` folder automatically:
```bash
uv venv
# Or for specific venv folder name (NOT recommended):
uv venv <venv_folder_name>
```

---
## 2) Still in the project root folder, active the virtual environment:
[/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

---
## 3) Check if the `.venv` is empty or with installed modules:
[/python/package-manager/uv/listing-installed-modules](/python/package-manager/uv/listing-installed-modules.md)

---

