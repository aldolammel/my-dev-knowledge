#### OS > Linux > Debian > Other apps
# Swing Music app

---

It's a Music player app based on Python.

---
## 1) Installing:
1.1) Create a venv;

1.2) Install Python 3.12;

==Be aware!==
Currently, jun/2026, the app is not compatible with Py 3.13+

1.3) Install the app:
Using PIP:
```
pip install swingmusic
```
Using UV:
```
uv add swingmusic
```

---
## 2) Integration:
2.1) Make it be a service to start up with the OS:
```
sudo nano /etc/systemd/system/swingmusic.service
```

2.2) File content:
```
[Unit]
Description=Swing Music
# Starts the service only after basic networking is available:
After=network.target

[Service]
# Adjust this according to your case:
User=<your_os_username>
# Adjust this according to your case:
WorkingDirectory=/media/shared-ssd/SwingMusicApp
# Adjust this according to your case:
ExecStart=/usr/local/bin/swingmusic
# Startup with OS and automatically restarts if it stops:
Restart=always

[Install]
WantedBy=multi-user.target
```
How to figure out your Linux current user on OS: [os/linux/command-change-user](os/linux/command-change-user.md)

2.3) Enable it:
```
sudo systemctl daemon-reload
sudo systemctl enable --now swingmusic
sudo systemctl status swingmusic
```

2.4) (If applicable) Case you need to edit the service file, after the edition, do it:
```
sudo systemctl daemon-reload
sudo systemctl restart swingmusic
sudo systemctl status swingmusic
```

2.5) (Optional) Once *Swing Music* app has no built-in metadata editor, you need an external solution:
- Using *Kid3*: [os/linux/distros/debian/1-apps-install/other-apps/kid3-metadata-editor](os/linux/distros/debian/1-apps-install/other-apps/kid3-metadata-editor.md)

---
## 3) Running it:
http://localhost:1970

==Important!==
Case you edit song's metadata through an external solution, you must restart the Swing Music service manually to see the changes:
```
sudo systemctl restart swingmusic
```

---
## 4) Updating:

4.1) Stop the service!
4.2) In another terminal, make sure you activated the app venv!
4.3) Update the app:
```
uv add "swingmusic==<version>"
```
E.g.
```
uv add "swingmusic==3.0.1"
```
4.4) Restart the service!

---
## This for Windows:
Soon!