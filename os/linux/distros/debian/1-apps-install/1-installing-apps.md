#### OS > Linux > Debian
# Installing apps

---
## Before:
1. Prepare the system: [/os/linux/distros/debian/1-apps-install/0-preparing-the-system](/os/linux/distros/debian/1-apps-install/0-preparing-the-system.md)
2. Install the basic apps, e.g., browser: [/os/linux/distros/debian/1-apps-install/basic-apps/using-apt/browser-firefox](/os/linux/distros/debian/1-apps-install/basic-apps/using-apt/browser-firefox.md)

---
## Install and uninstall apps:

==Important!==
When you run *sudo apt install <package_name>*, APT searches through its package index (a db of all available packages from repositories you've already added to your system). This index is created and updated when you run "sudo apt update".
### Installing

**From a repository (MOST USED):**
```
sudo apt install -y <package_name>        # -y skips install question!
```

Finding a package name installed: [/os/linux/distros/debian/1-apps-install/finding-installed-apps](/os/linux/distros/debian/1-apps-install/finding-installed-apps.md)

Check apt-update repo list: [/os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list](/os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list.md)

**From a local file:**
```
# Go to the installation file current folder and:
sudo apt install ./<file_name>.<file_extension>
```
E.g.
```
sudo apt install ./obsidian.deb
```
### Removing

**.deb:**
```
sudo apt remove <package_name>

# Clean up APT cache:
sudo apt autoclean

# Remove unused old apps/dependencies:
sudo apt autoremove
```
**Snap:**
```
sudo snap remove <app_name> || true
```


---
