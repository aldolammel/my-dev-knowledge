#### Python > Package Manager > UV

# Updating dependencies (command --upgrade)

The _uv --upgrade_ command automatically check if the dependency involved is compatible with, for example, the Django version you are using, avoiding those dependency versions that got known compatible issues.

---

## Before:

1. Upgrade UV itself: [[upgrade-uv]]

---

## 1) Make a choice:

- 1A) Update just a specific app dependency;
- 1B) Update all app dependencies (listed in pyproject.toml);

### 1A) Individual update

**Before:**

1. Open the project _pyproject.toml_ and check what you want to update next!

**1) Update the desired dependency:**

Mandatory ones, e.g.:

```
uv add "django-admin-sortable2>=2.2.7" --upgrade
```

Dev dependency ones, e.g.:

```
uv add "django-stubs[compatible-mypy]>=5.2.3" --upgrade --dev
```

A dependency from other sub-group, e.g.:

```
uv add "something>=3.0" --upgrade --subgrouphere
```

### 1B) Update everything listed in _pyproject.toml_

**Before:**

1. Only for Linux! Update and Upgrade your system: /vault/os/os/linux/debian/2-updates/update.txt

**1B.1) Update all dependencies:**

It removes all dependencies, and then install latest version of mandatory dependencies and dev ones as well:

```
uv sync --extra dev --upgrade
```

It removes all dependencies, and then install latest version of mandatory dependencies w/ multiple sub-grous:

```
uv sync --extra dev --extra test --upgrade
```

It removes all dependencies, and then install latest version of mandatory dependencies only (WARNING):

```
uv sync --upgrade
```

---

## 2) Check the _pyproject.toml_ if it looks fine!

---

## 3) Test your Python app to check if everything is going well.

---

**INSTALL DEPENDENCY:**
[[install-dependency]]

**UNINSTALL DEPENDENCY:**
[[uninstall-dependency]]
