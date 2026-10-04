#### Server > Web-server
# NginX

---

The "Engine-X" is is an open-source, a high-performance web server and reverse proxy server commonly used to:

- Serve websites and web applications;
- Load balance traffic across multiple servers;
- Act as a reverse proxy in front of apps;
- Cache content for faster delivery;
- Handle SSL/TLS termination (HTTPS).

**It’s popular because it is:**

- Very fast and lightweight;
- Good at handling many simultaneous connections;
- Widely used in modern cloud and containerized systems.
    
**Common uses:**
    
- Hosting websites;
- Running APIs;
- Kubernetes ingress controllers;
- Docker deployments;
- Micro-services gateways.
    
**Macro workflow:**

`Internet      ->    Webserver   ->   HTTP server  ->   App server/language`
It's the same to say:
`User Browser  ->    Nginx       ->   Gunicorn     ->   Python`

---
## NginX installation:
[install](/server/web-server/nginx/install.md)

---



