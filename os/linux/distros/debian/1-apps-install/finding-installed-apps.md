#### OS > Linux > Debian
# Finding APT installed apps

---

Finding all:
```bash
apt list --installed
```

Finding all with 'adobe' in the name:
```bash
apt list --installed | grep adobe             # <-- or "with quotes" for composed names.
```

Finding all with some 'obe' in the name:
```bash
apt list --installed | grep obe               # <-- It'll find all Adobe stuff.
```

Finding all the initial letters are 'web':
```bash
apt list --installed | grep ^web
```

---
## CHECK CURRENT REPO LIST:
[/os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list](/os/linux/distros/debian/1-apps-install/checking-app-is-in-repo-list.md)


