#### Python
# Language installation

---

## Before:

1. [ ] Check if Python is already installed:
	1. If Global, make sure you are NOT in any venv, and then: `$ python3 --version`
	2. If by project, assuming you activated the right venv folder, and then: `$ python3 --version` or `$ uv run python --version`
2. [ ] Case you wanna uninstall it:
	1. Uninstall the global installation: [Uninstall Python](/python/1-python-installation/uninstall.md)
	2. Uninstall the project installation: [/python/package-manager/uv/uninstall-python-old-version](/python/package-manager/uv/uninstall-python-old-version.md)

## 1) Which installation approach do you want:

- 1A) Using UV (by project, RECOMMENDED)
- 1B) Old style (global);

### 1A) Using UV (by project)

- [ ] **Before:**
1. Assuming you got UV installed: [/python/package-manager/uv/_about-install-and-update](/python/package-manager/uv/_about-install-and-update.md)
2. Assuming you're activated in the project venv.

- [ ] **Installing by project:** [/python/package-manager/uv/install-python-with-uv](/python/package-manager/uv/install-python-with-uv.md)
- [ ] Check the installation: `$ uv run python --version`

### 1B) Or using old style (global)

- [ ] **Before:**
1. Assuming you are NOT with a project venv activated.

- [ ] Update the local repository info:
```bash
sudo apt update
```
- [ ] Installing Python:
```bash
sudo apt install -y python3.14
```
- [ ] Check the installation: `$ python3 --version`
- [ ] Still with no project venv activated, install basic system-wide Python tools on VPS: `$ sudo apt install -y build-essential libssl-dev zlib1g-dev`
	- **build-essential:** gcc/make, required to compile any C extension packages.
	- **libssl-dev:** SSL support (Flask, requests, etc.).
	- **zlib1g-dev:** Compression support.


---
## Python uninstall
[uninstall](/python/1-python-installation/uninstall.md)

