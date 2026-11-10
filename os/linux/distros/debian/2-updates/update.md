#### OS > Linux > Debian
# Updating the system

---

Update the repositories list:
```bash
sudo apt update
```
Install the available updates:
```bash
sudo apt upgrade
```
Removes all dependencies installed but not needed anymore:
```bash
sudo apt autoremove
```
Cleans the local package cache by removing downloaded obsolete files:
```bash
sudo apt autoclean
```
Or:
```bash
sudo apt full-upgrade -y
```

---
## Changing/Upgrading the distro LTS version:
[/os/linux/distros/debian/2-updates/changing-LTS-version](/os/linux/distros/debian/2-updates/changing-LTS-version.md)
