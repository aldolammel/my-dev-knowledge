#### OS > Linux

# Before to format the current distro

---

## 1) Backup all non-clouded-files.

1.1) For workstation, save the .env files for each project once they're not on versioning.

---

## 2) Download distro .iso file.

**Make a choice:**
- Debian: https://debian.org
- Debian/Ubuntu: https://releases.ubuntu.com
- Fedora: https://fedoraproject.org

---

## 3) With the distro .iso available locally, mount it in a USB drive (>=8GB):

==Crucial!==
Don't use an external HD, except if you can use it entirely, without to use multiple partitions.

**3.1) Format the device where you will set the .iso (format to Ext4 format);**

**3.2) Check if your Ubuntu already brings the "Startup Disk Creator" and open it. If not, install it:**

[[systemtool-startup-disk-creator]]

**3.3) Select the .iso file and what storage device the creator should mount the selected file.**

---

## 4) Set the "Secure Boot" mode in BIOS (this avoid lot of headaches):

/vault/bios/secure-boot.txt

---

## 5) Let's format the system:

[[distro-formatting]]

---
