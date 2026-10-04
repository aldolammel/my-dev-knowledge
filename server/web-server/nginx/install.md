#### Server > Web-server > NginX
# Nginx installation

---
## Before:

1. About NginX: [\_about](/server/web-server/nginx/_about.md).
2. Assuming you are NOT activated on any venv.
3. Check if you already have it: `nginx -v`
4. If you have it, consider to update it, skipping this roadmap, going straight to: [update](/server/web-server/nginx/update.md)

---

==Crucial==
Nginx is a system-level service, so it must be installed always globally in the OS!

---      
## 1) Installing:
            
Debian/Ubuntu:
```bash
sudo apt install -y nginx
```
            
Windows:
```shell
xxxxxxxxxxxxxxxx
```
            
Mac:
```shell
xxxxxxxxxxxxxxxx
```

---
## 2) Integrating:

2.1) (If applicable) Include the Nginx service in your current firewall rules!
2.2) Test it!

### Testing via Debian
```bash
sudo systemctl enable nginx
sudo systemctl start nginx
sudo systemctl status nginx
```

**Case this error message:**
```bash
"Job for nginx.service failed because the control process exited with error code.
See "systemctl status nginx.service" and "journalctl -xeu nginx.service" for details."
```
Probably you got another process listening on port `80`. Check it out:
```bash
sudo ss -tlnp | grep ':80 '
```
If it's a Nginx conflict with another of its process, kill all of them, and restart the Nginx:
```bash
sudo pkill nginx
sudo systemctl start nginx
sudo systemctl status nginx
sudo ss -tlnp | grep ':80 '
# It's fine to see more than one NginX process listed in this case!
```
If it's the [Apache web-server](/server/web-server/apache/_about.md) that is listening on port `80`, try one of these options listed here: [/server/web-server/apache/uninstall](/server/web-server/apache/uninstall.md)
### Testing via Windows
```shell
xxxxxxxxxxxx
```
### Testing via Mac
```shell
xxxxxxxxx
```

---

## How to make NginX and Apache works through different ports:
[/server/web-server/apache-and-nginx-at-same-time](/server/web-server/apache-and-nginx-at-same-time.md)
