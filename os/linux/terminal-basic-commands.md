#### OS > Linux
# Terminal basic commands
---
## List directories:
```
ls
```
 Or to show **hidden** files and folders:
```
 ls -a
```

---
## Check the current path:
```
pwd
```

---
## Get it:
In a folder:
```
cd <folder_name>
```
Return one folder back
```
cd ..
```
In a text file:
```
nano <filename>
```

---
## Create:
Folder:
```
mkdir <folder name>
```
File:
```
nano <filename.extension>
```

---
## Rename:
Folder:
```
mv <current_foldername> <new_foldername>
```
File:
```
mv <current_filename.ext> <new_filename.ext>
```

---
## Delete:
Folder:
```
rm -r <folder_name>
```
File:
```
rm <filename.ext>
```

---
## Finding apps in the system:

- Debian: [/os/linux/distros/debian/1-apps-install/finding-installed-apps](/os/linux/distros/debian/1-apps-install/finding-installed-apps.md)
- Fedora: [/os/linux/distros/fedora/1-apps-install/finding-installed-apps](/os/linux/distros/fedora/1-apps-install/finding-installed-apps.md)

---
## Helpers:

How to start, stop, and check a service. Let's use the *PostgreSQL* service as example:
```
sudo systemctl status postgres
sudo systemctl start postgres
sudo systemctl stop postgres
sudo systemctl restart postgres
```

How to learn more about a command:
```
man <command you are trying to understand>
man postgres
```

---
## Switch current user on terminal:

[/os/linux/command-change-user](/os/linux/command-change-user.md)

