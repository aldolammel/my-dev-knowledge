#### Server > Web-server > Apache
# Apache uninstall

---

**You have 3 ways:**
1. A) Uninstall Apache completely.
2. B) Or just deactivate it.
3. C) Or change what port it should listening.

### A) Uninstall Apache completely
```bash
sudo apt purge apache2 apache2-bin apache2-data apache2-utils
sudo apt autoremove
```
Check if it still exists:
```bash
sudo systemctl status apache2
systemctl is-enabled apache2
```

### B) Or just deactivate the Apache
```bash
sudo systemctl disable --now apache2
# Make sure apache was stopped:
sudo systemctl status apache2
```
Check if Apache service will be restarted on the machine boot:
```bash
systemctl is-enabled apache2
# if returns "disabled" = won't be automatically restarted.
```

### C) Or change what port Apache should listening
[/server/web-server/apache-and-nginx-at-same-time](/server/web-server/apache-and-nginx-at-same-time.md)

---

