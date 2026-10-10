#### Python
# `pyproject.toml` file

---

The `pyproject.toml` file is an official Python standard configuration file (defined by PEP 518 and PEP 621) used across the entire Python ecosystem, mainly by  [UV package manager](/python/package-manager/uv/_about-install-and-update.md). This exists to define project metadata, dependencies, build systems, and tool configurations (like Ruff, Black, or pytest) in one centralized place. 

The simplification (and older) of this is the [requirements.txt](/python/requirements-txt.md) used by PIP.

---
## Project's dependency versions

==Critical to understand:==
Once the `pyproject.toml` declares what the project needs, the `uv.lock` (automatically created by [uv init command](/python/package-manager/uv/uv-init.md)) records exactly what was resolved/installed into the `.venv` folder. It's crucial to have `uv.lock` synced with `pyproject.toml` file, so every version tweaked in there must be followed by running [uv sync command](/python/package-manager/uv/uv-sync.md) in order to get the `uv.lock` file and `.venv` folder updated!

File: `/project_root_folder/pyproject.toml`:
```toml
[project.urls]
"Homepage" = "https://xxxxxxxxxxxxxxxxxxx"
"Repository" = "https://github.com/xxxxxxxxxxx/"
"Documentation" = "https://github.com/xxxxxxxxxxxxxxx/README.md"
"Bug Tracker" = "https://xxxxxxxxxxxxxxx"

[project]
name = "xxxxxxxxxxxxxxxxxx"
version = "0.1.0"  # There is a way to make it dynamic with repository!
description = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
readme = "README.md"
requires-python = ">=3.13, <=3.14" # or "==3.13.9"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "xxxxx@xxxxxx.com"}
]
maintainers = [
    {name = "Your Name", email = "xxxxx@xxxxxx.com"}
]
keywords = ["xxxx", "yyyyyyy", "zzzzzzzz"]
classifiers = [
    "Development Status :: 4 - Beta"
]
# App-level Core Dependencies:
# Remember 1: Server level dependencies will never (and shouldn't) be listed in pyproject file!
# Remember 2: after any version tweak, run 'uv sync' (if dev/qa env) or 'uv sync --group prod --locked --no-dev' (if uat/prod env)!
dependencies = []

# App-level Non-Core Dependencies:
[dependency-groups]
# Remember 1: Server level dependencies will never (and shouldn't) be listed in pyproject file!
# Remember 2: after any version tweak, run 'uv sync' (if dev/qa env) or 'uv sync --group prod --locked --no-dev' (if uat/prod env)!
dev = []
test = []
docs = []
prod = []

# Python Linter and Formatter:
# Reserved space...
```


---
