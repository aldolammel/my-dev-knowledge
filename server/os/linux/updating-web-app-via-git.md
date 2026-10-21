#### Server > OS > Linux > VPS
# Updating a web app

---
## Before:

PRE) Keep in mind:

Your current app files:
Keep your app GIT repo accessible on the browser JUST for you. e.g.:
https://github.com/xxxxxxxxxx/tree/main

Your current app main domain:
E.g.
http://vpsXXXXX.publicExample.com

Your current app path on server:
E.g.
```bash
cd /var/www/<app_name_folder>
```

        Updating database:
            For tiny apps, I like to store the db locally inside de project folder, so it would be in the repo too ("instance" folder).


---
## 1) Updating files:

        1.1) Connect to the server:
[/server/connecting-via-ssh](/server/connecting-via-ssh.md)

        1.2) Update the app repository:
[/versioning/git/command-pull](/versioning/git/command-pull.md)

        1.3) Refresh the communication (service) between the web server and the app, restarting the Gunicorn (WSGI):
```bash
sudo systemctl restart <simplified_app_name>
systemctl status <simplified_app_name>
```

            DID YOU FORGET THE SERVICE NAME?
```bash
sudo systemctl list-units --type=service
# Probably this list will help you to figure it out!
```

---
## 2) Something wrong? Try it:
Restart the web server:
```bash
sudo systemctl restart nginx
systemctl status nginx
```

Restart the communication (service) between the web server and the web app:
```bash
sudo systemctl restart <simplified_app_name>
systemctl status <simplified_app_name>
```

Nothing yet? Restart the server and repeat this entire step:
```bash
sudo reboot
```

---
## 3) Updating database:

I'm currently using the portfolio repo to store the DB ("instance" folder).

---


