**Option B: Keep Apache, move nginx to another port**

Edit the default site and change the listen lines:

bash

```bash
sudo nano /etc/nginx/sites-available/default
```

nginx

```nginx
listen 8080 default_server;
listen [::]:8080 default_server;
```

Then:

bash

```bash
sudo nginx -t && sudo systemctl start nginx
```

**Verify afterwards:**

bash

```bash
curl -I http://localhost
```

You should see `Server: nginx/1.28.3` in the response headers.