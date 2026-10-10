#### Server > Tools > For Python
# Gunicorn installation

---

Gunicorn is a Python WSGI HTTP server (Web Server Gateway Interface). It's the bridge between your Python app and the outside world (internet):

So it's a [production-only](/dev-concepts/environment-production-prod.md) server.

`Internet      ->    Webserver   ->   HTTP server  ->   App server/language`
It's the same to say:
`User Browser  ->    Nginx       ->   Gunicorn     ->   Python`

---

## 1) Make a decision:
    
- 1A) Installation by project (RECOMMENDED).
- 1B) Global installation.

......................................

### 1A) By project
        
- [ ] **Before:**
1. Assuming you are working in the [prod environment](/dev-concepts/environment-production-prod.md) server.
2. Assuming you are in the app venv!
        
- [ ] **Installation:**

Using UV: 
```bash
uv add --group prod gunicorn
```

Or using PIP:
```bash
sudo pip install gunicorn  
```
And make sure you have this in your `requirements-prod.txt` or in the prod group in `pyproject.toml`.

......................................

### 1B) Globally
        
- [ ] **Before:**
1. Assuming you are working in the [prod environment](/dev-concepts/environment-production-prod.md) server.
2. Assuming you are NOT in a app venv!

- [ ] **Installation:**
- Using a distro built-in package manager:
	- Debian/Ubuntu: `$ sudo apt install gunicorn`
	- Or Fedora: `$ sudo dnf install gunicorn`
- Or using UV but first, UV will:
	- create an isolated virtual environment for Gunicorn;
	- expose the Gunicorn executable globally in your user PATH;
	- avoid polluting the system Python.
	- That said, do it: `$ uv tool install gunicorn`

---

