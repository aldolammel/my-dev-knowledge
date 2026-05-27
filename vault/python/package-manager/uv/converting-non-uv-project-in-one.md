#### Python > Package Manager > UV
# Converting *requirements.txt* file to *pyproject.toml*

==Be aware!==
Avoid to use the *uv pip install -r requirements.txt* command once it will not update automatically your *pyproject.toml*, and to keep a project using the *requirement.txt* method is not reliable in long-term.

If you wanna convert an existing project to use UV as its package manager, including all basic package management files to replace *requirements.txt*, do it:

## Before:
1. In the existing project folder, install UV: [[_about-install-and-update]]

## 1) There, active the local environment and execute *uv init*!
It will create the basic scaffolding files in the project!

## 2) Take the current *requirements.txt*:
And rewrite each requirement for UV format, installing all of them (and automatically include them in *pyproject.toml* file as well). E.g.
```
uv pip install "Flask~=3.0.2" "SQLAlchemy~=2.0.27" "flask-sqlalchemy~=3.1.1" "Bootstrap-Flask~=2.3.3" "jinja2~=3.1.3"
```

## 3) Make sure your *pyproject.toml* file is updated in those requirements:
And, then, delete the *requirements.txt* file from the project!
