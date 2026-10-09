#### Python > Package Manager > UV
# Updating dependencies

---

The `--upgrade` flag in UV command automatically checks if the dependency involved is compatible with, for example, the Django version you are using, avoiding those dependency versions that got known compatible issues.

---

## Before:

1. Upgrade UV itself: [/python/package-manager/uv/upgrade-uv](/python/package-manager/uv/upgrade-uv.md)
2. Assuming you are in the project root folder.
3. Open the project `pyproject.toml` and check if all dependencies (core and dev) have their limit versions correct!
4. Remember: `pyproject.toml` only sets limits. The real list of which versions are installed is in `uv.lock` file (automatically edited by UV commands).

---
## 1) Check those dependencies that have update available:
This will show just the current installed version versus the latest version available:
```bash
# Simplify view:
uv tree --outdated --depth 1 --all-groups
# Or complete view:
uv tree --outdated --all-groups
```

---
## 2) Make a choice:

- 2A) Update a specific app-level installed (core or dev) dependency.
- 2B) Update all app-level installed (core and dev) dependencies.
- 2C) Update only app-level installed core dependencies.

......................................
### 2A) Update a specific app-level installed (core or dev) dependency

Updating a core dependency, e.g.:
```bash
uv add "django-admin-sortable2>=2.2.7" --upgrade  # To define a specific version, you can use ==.
```

Updating a dev dependency, e.g.:
```bash
uv add "django-stubs[compatible-mypy]>=5.2.3" --upgrade --dev  # To define a specific version, you can use ==.
```

Updating a dependency from another sub-group, e.g.:
```bash
uv add "something>=3.0" --upgrade --subgrouphere  # To define a specific version, you can use ==.
```

......................................
### 2B) Update all app-level installed (core or dev) dependencies

Removes and re-installs all core and dev dependencies in their latest versions or highest versions you've defined via `pyproject.toml` allows them:
```bash
uv sync --extra dev --upgrade
```

Example if you need to update more sub-groups than dev only:
```bash
uv sync --extra dev --extra test --upgrade
```

......................................
### 2C) Update only app-level installed core dependencies

Removes and re-installs all core dependencies only in their latest versions or highest versions you've defined via `pyproject.toml` allows them:
```bash
uv sync --upgrade
```

---
## 3) Final double-checks:

3.1) Open the pyproject.toml and make sure everything about dependencies make sense for your;

3.2) Even though [uv sync command](/python/package-manager/uv/uv-sync.md) already executes the [uv lock command](/python/package-manager/uv/uv-lock.md) behind the scene, run it manually:
```bash
uv lock --check
```

3.3) Test your Python app to check if everything is going well: [/python/web-development/django/\_running-app](/python/web-development/django/_running-app.md)

---
## Installing an app-level dependency:
[/python/package-manager/uv/install-dependency](/python/package-manager/uv/install-dependency.md)
## Uninstalling an app-level dependency:
[/python/package-manager/uv/uninstall-dependency](/python/package-manager/uv/uninstall-dependency.md)

