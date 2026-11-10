#### OS > Linux > Fedora
# Updating the system

---

0. (Optional) Only update the repositories list:
```bash
sudo dnf check-update
```
1. Update the repositories and install the available updates:
```bash
sudo dnf upgrade
```
2. Removes orphaned dependency packages that were installed automatically but are no longer needed by any installed app:
```bash
sudo dnf autoremove
```
3. Cleans the local package cache by removing downloaded obsolete files:
```bash
sudo dnf clean all
```

---
## Changing Fedora version:
This safely upgrades your existing installation to the next release version (e.g., Fedora 42 to 43) without losing your files or settings.
Download the new release packages:
```bash
sudo dnf system-upgrade download --releasever=43
```
Trigger the upgrade and reboot:
```bash
sudo dnf system-upgrade reboot
```

---


