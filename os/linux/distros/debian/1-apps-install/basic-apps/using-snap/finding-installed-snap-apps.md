#### OS > Linux > Debian
# Finding installed snap apps

---

Finding all:
```
snap list
```

Finding all with 'adobe' in the name:
```
snap list | grep firefox             <-- or "with quotes" for composed names.
```

Finding all with some 'fire' in the name:
```
snap list | grep fire               <-- It'll find all Firefox stuff.
```

Finding all the initial letters are 'web':
```
snap list | grep ^web
```

---
## Uninstalling a snap app:
[\_uninstall-snap-apps](os/linux/distros/debian/1-apps-install/basic-apps/using-snap/_uninstall-snap-apps.md)
## Installing a snap app:
Ubuntu default store!
