#### Python > Components & Libraries
# Gettext

---

It's the standard toolkit for translations across many languages (Python, Perl, Ruby, Lua) and frameworks. The Gettext module is a core part of Python's standard library that provides internationalization (i18n) and localization (l10n) services for Python apps.

---
## Installation:

**Before:** assuming you are NOT using virtual environment now.

**Installing globally:**
```bash
sudo apt update
sudo apt install gettext
```
### Exception case (Alternative)

Case the server doesn't allow you to use `apt install`, alternatively you can use (not recommended) a project isolated solution:

==Critical==
Don't use this in cause you have permission to use `apt install` in project machine.

**Before:** Make sure you ARE activated in the project environment. 

**Install it:**
```bash
# Using UV:
uv add python-gettext
# Using PIP:
pip install xxxxxx
```

---
## Integration:
[/python/web-development/django/8-translate-and-internationalization/1-starting-translation](/python/web-development/django/8-translate-and-internationalization/1-starting-translation.md)

---

