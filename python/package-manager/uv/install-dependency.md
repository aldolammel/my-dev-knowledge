#### Python > Package Manager > UV
# Installing Dependencies


---

## Before:
1. What is it:  [[_about-install-and-update]] 
2. Avoid to use *uv pip install <package_name>* once this command doesn't automatically update crucial files in a project like *uv.lock* and *pyproject.toml*.



---


## 1) Installing:

Installing mandatory dependency:
```
uv add <package_name>
```

Installing optional dependency:
```
uv add --optional <sub-group> <package_name>
```
E.g.
```
uv add --optional dev ruff
```

Checking installed ones:
```
uv pip list
```


---


**Update dependencies:**

[[upgrade-dependencies]]

**Uninstall dependency:**

[[uninstall-dependency]]