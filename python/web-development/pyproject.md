#### Python
# pyproject.toml file

---

Basically, it declares what the project needs!

The `pyproject.toml` file is a standard configuration file used in Python projects to define project metadata, dependencies, build systems, and tool configurations (like Ruff, Black, or pytest) in one centralized place. 

---
## Project's dependency versions

==Critical to understand:==
Once the `pyproject.toml` declares what the project needs, the `uv.lock` (automatically created by [uv init command](/python/package-manager/uv/uv-init.md)) records exactly what was resolved/installed into the `.venv` folder. It's crucial to have `uv.lock` synced with `pyproject.toml` file, so every version tweaked in there must be followed by running [uv sync command](/python/package-manager/uv/uv-sync.md) in order to get the `uv.lock` file and `.venv` folder updated!

File: `pyproject.toml`:
```toml
[project.urls]
"Homepage" = "https://xxxxxxxxxxxxxxxxxxx"
"Repository" = "https://github.com/xxxxxxxxxxx/"
"Documentation" = "https://github.com/xxxxxxxxxxxxxxx/README.md"
"Bug Tracker" = "https://#"

[project]
name = "xxxxxxxxxxxxxxxxxx"
version = "0.1.0"  # There is a way to make it dynamic with repository!
description = "xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
readme = "README.md"
requires-python = ">=3.13, <=3.14" # or "==3.13.9"
license = {text = "MIT"}
authors = [
    {name = "Aldo Lammel", email = "xxxxx@xxxxxx.com"}
]
maintainers = [
    {name = "Aldo Lammel", email = "xxxxx@xxxxxx.com"}
]
keywords = ["xxxx", "cccccc", "vvvvvvv"]
classifiers = [
    "Development Status :: 4 - Beta"
]
# App-level Core Dependencies:
# Remember 1: Server level dependencies will never (and shouldn't) be listed here!
# Remember 2: after any version tweak, run 'uv sync --extra dev' (if dev env) or 'uv sync' (if prod env)!
dependencies = []

# [dependency-groups]
# Don't use it 'coz it's not compatible with many tools!
# That said, keep using [project.optional-dependencies].

# App-level Dev Dependencies:
[project.optional-dependencies]
# Remember 1: Server level dependencies will never (and shouldn't) be listed here!
# Remember 2: after any version tweak, run 'uv sync --extra dev' (if dev env) or 'uv sync' (if prod env)!
dev = []
test = []
docs = []

# Python Linter and Formatter:
# Reserved space...
```