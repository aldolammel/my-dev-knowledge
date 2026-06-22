#### OS > Linux > Debian > New OS installation
# Right after the system installation

---
## 1) Turn the "Secure Boot" off:

[/bios/secure-boot](/bios/secure-boot.md)

---
## 2) Check if all basic motherboard settings are okay for your system:

[/bios/basic-modo-settings](/bios/basic-modo-settings.md)

---
## 3) (If applicable) If you are using Ubuntu <26

Keep using "Ubuntu (Xorg) session" in login-screen. "Wayland" keeps too buggy in current LTS <26. From LTS 26 and so on there's no Xorg anymore!

---
## 4) First system log-in:

**4.1) Preparing the system:**

[os/linux/distros/debian/1-apps-install/0-preparing-the-system](os/linux/distros/debian/1-apps-install/0-preparing-the-system.md)

**4.2) Display and sound configs;**

**4.3) Install your default browser:**

E.g. [os/linux/distros/debian/1-apps-install/basic-apps/using-apt/browser-firefox](os/linux/distros/debian/1-apps-install/basic-apps/using-apt/browser-firefox.md)

**4.4) (If applicable / Optional) If you are using Debian (any version) or Ubuntu <26:**

Install this smarter terminal: [os/linux/distros/debian/1-apps-install/basic-apps/using-flatpak/terminal-ptyxis](os/linux/distros/debian/1-apps-install/basic-apps/using-flatpak/terminal-ptyxis.md)

**4.5) (If applicable / Optional) If you are not using the *Ptyxis* terminal:**

Customize the Terminal: [os/linux/distros/debian/1-apps-install/basic-apps/terminal-CLI-oh-my-bash](os/linux/distros/debian/1-apps-install/basic-apps/terminal-CLI-oh-my-bash.md)

---
## 5) Making Linux mount shared SSDs automatically:

[os/linux/distros/debian/mounting-shared-drives-automatically](os/linux/distros/debian/mounting-shared-drives-automatically.md)

---
## 6) Check if IPv6 is working properly:

Some website hosts don't work through IPv4 preferentially, making a few websites get stuck in loading:

https://askubuntu.com/a/1554260/1731699

---
## 7) (if applicable) If you are using dual-boot:

In case you are using Dual-boot with Windows, set Windows to use UTC time, equal to Ubuntu, for compatibility with Dual-boot;

==Important!==
Linux works better with UTC instead of Local Time.

[os/windows/0-os-install/dual-boot-with-linux](os/windows/0-os-install/dual-boot-with-linux.md)

---

**THE ENTIRE LINUX FORMATTING ROADMAP:**

[os/windows/0-os-install/\_roadmap](os/windows/0-os-install/_roadmap.md)
