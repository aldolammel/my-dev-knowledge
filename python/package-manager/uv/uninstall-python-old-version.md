#### Python > Package Manager > UV

# Uninstalling a specific Python version

==Be aware!==
You are able to uninstall Python through UV only if you installed Python [using UV method](install-python-with-uv.md). Otherwise, uninstall Python using the traditional way (/python/1-python-installation/uninstall.txt).

---

## 1) Checking all Python versions installed:

```
uv pip tree
```

or

```
uv run python --version
```

---

## 2) Uninstalling:

Uninstalling a specific version:

```
$ uv python uninstall 3.13
```

---
