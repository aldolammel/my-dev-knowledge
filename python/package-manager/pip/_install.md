#### Python > Package manager
# PIP (Python built-in package manager)

---

==Attention==
UV is much more efficient and modern than PIP: [/python/package-manager/uv/\_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)

---

It's a package manager for Python packages, or modules if you like. Note: If you have Python version 3.4 or later, PIP is included by default.

## Before:

1. Make sure you are in the right Python Interpreter in your IDE.
	1. PyCharm: check the right-lower-corner;
	2. VSCode: press Ctrl+Shift+P and type 'Python Interpreter'
2. Active your environment: [/python/3-virtual-environment/activate-and-deactivate](/python/3-virtual-environment/activate-and-deactivate.md)

---
## Installing

**Windows:**
```shell
py -m pip install --upgrade pip
```
    
**Debian & Ubuntu:**
Just for make sure even the system apps list is updated:
```bash
sudo apt update
```
    
Specific for Ubuntu:
Pip already comes with Python installation, so just update it!
```bash
python3 -m pip install --upgrade pip
```
            
Specific for Debian:
Pip is not bundled with Python (even though it's the Python built-in package manager)!
```bash
sudo apt install -y pip
```
        
**Mac:**
```bash
python3 -m pip install --upgrade pip
```

---

