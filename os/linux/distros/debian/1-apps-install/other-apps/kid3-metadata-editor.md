#### OS > Linux > Debian > Other apps
# Kid3 Metadata editor

---

This is needed if you want to edit your song's metadata case your Music player has no built-in metadata editor like [Swing Music app](/os/linux/distros/debian/1-apps-install/other-apps/swing-music.md).

---
## 1) Installing:

```
sudo add-apt-repository ppa:ufleisch/kid3
sudo apt update
```
For KDE users:
```
sudo apt install kid3
```
Or without KDE dependencies:
```
sudo apt install kid3-qt
```
For the command-line interface:
```
sudo apt install kid3-cli
```

## 2) Running:

If KDE users:
```
kid3
```
If no KDE:
```
kid3-qt
```
