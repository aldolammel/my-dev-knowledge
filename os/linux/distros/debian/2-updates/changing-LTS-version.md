#### OS > Linux > Debian
# Changing/Upgrading the LTS version

---

## Before:
1. Backup your important stuff!


---

## 1) Tell OS to upgrade to the newest LTS:

Do it just if the LTS was officially released:
```
sudo do-release-upgrade
```
Or if the latest LTS still in the earlier days where the first hotfix wasn't release yet:
```
sudo do-release-upgrade -d
```


---

## 2) Update the new system:

[os/linux/distros/debian/2-updates/update](os/linux/distros/debian/2-updates/update.md)


---

## 3) Reboot:
```
sudo reboot
```


---

## For Fedora distro:

[os/linux/distros/fedora/2-updates/changing-LTS-version](os/linux/distros/fedora/2-updates/changing-LTS-version.md)

## Or just updating the current distro:

[os/linux/distros/debian/2-updates/update](os/linux/distros/debian/2-updates/update.md)
