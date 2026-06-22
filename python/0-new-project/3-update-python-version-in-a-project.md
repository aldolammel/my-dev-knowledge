#### Python > Project types
# Updating Python version in an existing project

---

# Updating Python in an existing project

==Critical!==
Are you really sure the Python version you need to install is compatible with other techs of the project stack? For example, the back-end framework you are using supports this new Python version? If so, keep going!


---

## 1) Make a choice, which tool are you using:
- 1A) Using Python only;
- 1B) Using UV package manager;

### 1A) Using Python only

**Before:**
1. xxxxx

**A.1) xxxxxxxxxxxx**

**A.2) xxxxxxxxxxxx**

### 1B) Using UV

**Before:**
1. Assuming you already got UV installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

**1B.1) Check the current Python versions installed and install that you need:**

In your global local environment, check it:
```
uv python list
```
Add the new one, e.g.:
```
uv python install 3.13.9
```


1**B.2) In your project folder/environment, set up:**

Defining to UV which Python version the project must run, e.g.:

[/python/package-manager/uv/pin-python-version](/python/package-manager/uv/pin-python-version.md)

1B.2.1) (If applicable) In *pyproject.toml* file, update Python version:
```
[project]
...
requires-python = "==3.13.9"  # Or ">=3.13.7,<3.14"
```
1B.2.2) (If applicable) In *pyproject.toml* file, if using *Ruff*:
```
[tool.ruff]
...
target-version = "py313"  # Python (py313 means newest of 3.13 = 3.13.9) <------
```
1B.2.3) (If applicable) In *pyproject.toml* file, if using *MyPy*:
```
[tool.mypy]
...
python_version = "3.13"  # 3.13 means newest of 3.13 = 3.13.9  <----------------
```
1B.2.4) Sync the environment (UV will recreate *venv* with new Python):

[/python/package-manager/uv/auto-installation-with-sync](/python/package-manager/uv/auto-installation-with-sync.md)

1B.2.5) Deactivate and active the project environment:

[/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

1B.2.6) Verify the Python version in the environment:
```
uv run python --version
```

**1B.3) (Optional) Uninstall unwanted Python versions:**

[/python/package-manager/uv/uninstall-python-old-version](/python/package-manager/uv/uninstall-python-old-version.md)


---
