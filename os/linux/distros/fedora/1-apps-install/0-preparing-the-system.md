#### OS > Linux > Fedora > New OS installation
# Preparing the system

---
## 1) Install dependencies (this ensures your system is ready to add new repositories):
```
sudo dnf update && sudo dnf upgrade -y
```
And then:
```
sudo dnf install software-properties-common apt-transport-https wget gpg -y
```

---
## 2) Install flatpak support (alternative to Snap and .deb):

```
sudo dnf install -y flatpak
```
Add Flathub repository:
```
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
```

---
## 3) Research which is the current and best Nvidia driver for your VGA card:

3.1) Basic: e.g. in Feb/2026 with a RTX3070:
```
sudo dnf install -y nvidia-driver-590-open
```
AI prompt:
```
In Fedora <version>, I am using a Nvidia GeForce RTX3070 with 3 monitors. How do I check the best current driver for it through the terminal?
```

3.2) Expanding VGA usage with AI (Install CUDA):

https://developer.nvidia.com/cuda/toolkit

Ubuntu official repos already provide future CUDA updates when it's installed.

---
## 4) Installing the KDE Desktop environment for Fedora:

Even using Gnome as interface, the Fedora UX is not good, so the KDE interface is necessary for long-term use:
```
sudo dnf group install kde-desktop-environment
```
(Optional) Basic KDE apps:
```
sudo dnf group install kde-apps
```

Switch to KDE interface:
1. **Reboot** or **Log out** of your current session.
2. On the login screen, click on your username.
3. Before typing your password, look for a **gear icon** (usually in the bottom-right corner).
4. Click it and select **Plasma**.
5. Enter your password and log in.

---

## INSTALLING THE BASIC APPS:

/os/linux/distros/fedora/1-apps-install/basic-apps/

