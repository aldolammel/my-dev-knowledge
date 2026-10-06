#### Python > Project types
# Discovery

---
## Before:

1. Did you collected every pain-point from the IT leader/stakeholder of this product?
2. It could be great if you would have access to the product's *Technical Design Document* (TDD) or, at least, to the *ERD* document (how really complex is this back-end product)! 

---
## 1) Python version installed:

**Make a decision:**

- A) Using UV.
- B) Using Python/PIP.

......................................

**A) Using UV:**

A1) Assuming you already got UV installed: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

A2) Make sure the project is using Python globally or locally!

A3) List all Python version installed:
```bash
uv python list
```

A4) Checking which version the project must use:
```bash
uv pin
# And take a note!
```

A5) Checking if project main requirement file has the same version declared:
- `.python-version`
- `pyproject.toml`
- `uv.lock`

......................................

**B) Using Python/PIP:**

B1) Make sure the project is using Python globally or locally!

B2) What Python version is installed?

B3) Checking if project main requirement file has the same version declared:
	- `.python-version`
	- `requirements.txt`

---
## 2) (If applicable) To update/upgrade:

==CRITICAL==
Any update/upgrade is NOT recommended until the discovery of the whole project layers (back-end + front-end) to be finished.

[/python/0-new-project/3-update-python-version-in-a-project](/python/0-new-project/3-update-python-version-in-a-project.md)

---
## 3) Discovery of project's Python framework:

- If it runs **Django**: [/python/web-development/django/0-new-project/discovery-django](/python/web-development/django/0-new-project/discovery-django.md)
- If it runs **Flask**: xxxxxxxxxxxxx
- If it runs **Fast-API**: xxxxxxxxxxxxxxx

---

