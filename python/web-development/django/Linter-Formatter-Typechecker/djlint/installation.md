#### Python > Linter, Formatter & Type checker
# DjLint: Installation and integration

---

## Before:

1. What is DjLint: [About](/python/web-development/django/Linter-Formatter-Typechecker/djlint/_about.md)

---
## Installing:

PRE) Assuming you already got a virtual environment for the project, active it: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

1.1) Install the djlint as development dependency:

            >> Using UV:
                $ uv add --optional dev djlint
                    # Check if everything's right on the project's pyproject.toml file!

            >> Or using PIP:
                # Install it:
                    $ python3 -m pip install -U djlint
                # And add this module as dev dependency in pyproject.toml (e.g.):
                    ...
                    [project.optional-dependencies]
                    dev = [
                        ...
                        "djlint>=1.36.4",
                    ]

---
## Integration:

2.1) Still in `pyproject.toml` file, add these lines:
```toml
# Django template Linter and Formatter:
[tool.djlint]
profile="django"
max_line_length = 100
preserve_blank_lines = true
close_void_tags = true
```

If Prettier or other CSS/JS formatter is ON in this project:
```toml
format_css = false  # false = Prettier should take care of it!
format_js = false  # false = Prettier should take care of it!
```

2.2) And manually install the DjLint extension for your Code IDE.

2.3) DjLint configuration on IDE:

            >> Using VSCode:

                PRE) Assuming you already have:
                    .../django/ide/vscode/examples/settings.json

                >> In /project/.vscode/settings.json, add the lines:

```json
// PYTHON SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
...
// DJANGO SETTINGS - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
...
"[django-html]": {
	"editor.defaultFormatter": "monosans.djlint", // DjLint
	...
},
```

---

