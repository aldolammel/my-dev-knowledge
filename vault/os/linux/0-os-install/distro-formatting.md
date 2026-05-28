#### OS > Linux

# Formatting the system


---

## Before:
1. Assuming you already have done basic to format: [[os/linux/0-os-install/before-to-format]]


---

## 1) Reboot the machine and get in your BIOS;


---

## 2) Override the boot order to use the bootable device in boot. Then reboot again;


---

## 3) When the Ubuntu options is shown, select "Install":

==If terminal is needed!==
In any moment of this install wizard, do Ctrl + Alt + F2.

**Basic terminal commands:**
[[os/linux/terminal-basic-commands]]

**Specific distro commands for:**
- Debian/ubuntu: [[os/linux/distros/debian/terminal-commands]]
- Fedora: [[os/linux/distros/fedora/terminal-commands]]


---

## 4) (If applicable) Case you select the manual installation:

The "Boot loader" is a super small partition automatically created during the partition table creation (last time you installed the system). In this small partition is where the "dual-boot menu" would be located!

After select the partition to install Ubuntu, make sure you are using Ext4 format and the root folder is "/" only.


---

## 5) Once the OS installation has finished, do this based on OS chosen:

- Debian/Ubuntu: [[os/linux/distros/debian/0-os-install/right-after-install]]
- Fedora: [[os/linux/distros/fedora/0-os-install/right-after-install]]

---


**THE ENTIRE LINUX INSTALLATION ROADMAP:**
[[os/linux/0-os-install/_roadmap]]
