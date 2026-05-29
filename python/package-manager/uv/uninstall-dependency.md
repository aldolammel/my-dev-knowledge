#### Python > Package Manager > UV
# Uninstalling dependencies



---


## Before:
1. What is it: [[_about-install-and-update]]


---

## 1) Remove the package from everywhere, regardless it's mandatory or optional:
```
uv remove <package_name>
```
Remove the package from a specific group of optionals:
```
uv remove --optional <sub-group> <package_name>
```
E.g. 
```
uv remove --optional dev ruff
```


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


**INSTALL DEPENDENCY:**

[[python/package-manager/uv/install-dependency]]

**UPDATE DEPENDENCY:**

[[upgrade-dependencies]]
