#### OS > Linux > Debian > apt
# System tool > Ptyxis Terminal

---

PRE) Assuming you already installed Flatpak support: [/os/linux/distros/fedora/1-apps-install/0-preparing-the-system](/os/linux/distros/fedora/1-apps-install/0-preparing-the-system.md)

---
## 1) Install Ptyxis:
```bash
flatpak install flathub app.devsuite.Ptyxis
```

---
## 2) Customize it:

2.1) Install a compatible font and set it as the font to be used in Terminal:
            "Fira Code"

                Using: Fire Code Regular 11

2.2) Palette = "Birds Of Paradise" or...
                        "Breath Silverfox"
                        "Broadcast"
                        "Chameleon"
                        "Solarized Darcula"
                        "Monokai Pro"

2.3) Other customs:
            - Line Spacing = 1,1
            - Blinking Text = Focused
            - Cursor Shape = Underline

---
## (Optional) Removing the Gnome Terminal:
```bash
sudo apt remove gnome-terminal
sudo apt autoremove --purge
```

---

XXXXXXXXXXXXXXXXX:
/xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
