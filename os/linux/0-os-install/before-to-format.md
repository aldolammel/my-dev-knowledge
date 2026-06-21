#### OS > Linux
# Before to format the current distro

---

## 1) Backup all non-clouded-files:

**1.1) Your development projects:**

Save .env files for every local projects you are developing once they shouldn't be available in the project's repository.

---

## 2) Download distro .iso file:

**Make a choice:**
- Debian: https://debian.org
- Debian/Ubuntu: https://releases.ubuntu.com
- Fedora: https://fedoraproject.org

---

## 3) With the distro .iso available locally, mount it in a USB drive (>=8GB):

==Crucial!==
Don't use an external HD, except if you can use it entirely, without to use multiple partitions.

**3.1) Format the USB drive:**
- Format the device where you will mount the .iso (format to Ext4 format).

**3.2) Startup disk creation:**
- Check if your current Linux distro already brings some kind of app for startup disks creation.
	- Debian and Ubuntu built-in solution: [[os/linux/distros/debian/1-apps-install/basic-apps/using-apt/systemtool-startup-disk-creator]]

**3.3) Select the .iso file and what storage device the creator should mount the selected file.**

---

## 4) Set the "Secure Boot" mode in BIOS (this avoid lot of headaches):

[bios/secure-boot](bios/secure-boot.md)

---

## 5) Let's format the system:

[os/linux/0-os-install/distro-formatting](os/linux/0-os-install/distro-formatting.md)


---
