#### Python > Linter, Formatter & Type checker
# MyPy

---

By Microsoft, it's an optional static type checker for Python that aims to combine the benefits  of dynamic (or "duck") typing and static typing. Mypy combines the expressive power and convenience of Python with a powerful type system and compile-time type checking.

https://mypy-lang.org/
        
---
## Installing:
        
### 1) Installing as development dependency

- [x] In the project folder, install the MyPy as development dependency:

Using UV:
```bash
uv add --optional dev mypy
# Check version:
uv pip show mypy
```

Using PIP:
```bash
python3 -m pip install mypy
# Check version:
pip show mypy
```
Case you used PIP, include it manually (adjusting the right MyPy version) in the project `pyproject.toml` file:
```toml
[project.optional-dependencies]
dev = [
	...
	"mypy>=1.17.1",  # Make sure this version make sense!
]
```

### 2) In your IDE

- [x] Install the 'MyPy Type Checker' extension (by Microsoft);

### 3) (If applicable / Optional) For Django projects, install the django-stubs

- [x] For Django projects, further you should install the django-stubs for better Django type hints! (We will see this in Integration steps!)
    
---
## Integration:

### Before
1. [x] Assuming you already got the `pyproject.toml` in your project: [/python/web-development/pyproject.toml](/python/web-development/pyproject.toml)
### 1) Add lines in `pyproject.toml`:
- [x] 1.1) Include these lines in your in your `pyproject.toml`: [/python/linter-formatter-typechecker/MyPy/pyproject.toml](/python/linter-formatter-typechecker/MyPy/pyproject.toml)

- [ ] 1.2) (If applicable / Optional) For Django projects, install the *django-stubs* for better Django type hints: [python/web-development/django/Linter-Formatter-Typechecker/django-stubs/_installation](python/web-development/django/Linter-Formatter-Typechecker/django-stubs/_installation.md)

### 2) (If applicable / Optional)
            In the project .vscode/settings.json, do it:

PRE) Assuming you have this file in the project:
                    /python/ide-softwares/vscode/examples/settings.json

2.1) Turn off the Pylance Type Checking, leaving this task only to MyPy:
                    
                    // PYTHON SETTINGS
                    ...
                    "python.analysis.typeCheckingMode": "off", // This project is using MyPy for Type Checking.

2.2) (Optional)
                    Still in .vscode/settings.json, add this:

                        // FILES
                        "files.exclude": {
                            ...
                            "**/.mypy_cache": true,
                        },
                        "search.exclude": {
                            ...
                            "**/.mypy_cache": true,
                        }

---
## How to ignore false-positive errors:
[/python/linter-formatter-typechecker/MyPy/ignoring-false-positive-errors](/python/linter-formatter-typechecker/MyPy/ignoring-false-positive-errors.md)