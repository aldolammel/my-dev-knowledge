

DEBIAN/UBUNTU > BUILDING UP A VPS: LATE CONFIGURATIONS


    PRE.1) Assuming you have finished the previous steps!
    
    
    PRE.2) Assuming you're in the VPS terminal, and in the app folder!
    
    
    PRE.3) Assuming you're using the right venv!
    
    
    PRE.4) Remember the code language port for your case:
        >> Python = 5000
        >> xxxxxxx = xxxx


    1) WSGI configuration:
    
        >> For Python projects:
    
            1.1) Make sure the wsgi.py is already:
                $ nano wsgi.py
                    E.g.
                        from main import app, db
                        if __name__ == "__main__":
                            with app.app_context():
                                db.create_all()
                            app.run()
                        
                # Save (ctrl+s) and exit (ctrl+x)
            
            1.2) Launching the production-ready Python web server to host the app:
                
                >> For UV users:
                    $ uv run gunicorn --bind 0.0.0.0:<code_language_port> wsgi:app
                        Output e.g.
                            [2026-05-21 11:01:12 -0300] [30652] [INFO] Starting gunicorn ...
                            ...
                
                >> Or directly through the venv:
                    $ .venv/bin/gunicorn --bind 0.0.0.0:<code_language_port> wsgi:app
                
                INFO:
                    Maybe it'll look like frozen terminal, but it's not. Just go to the next step (or for some reason, in order to abort, do Ctrl+C).
                    
                SOME ERROR?
                    Getting explicit error when you try to connect with 0.0.0.0:<code_language_port>?
                        Probably something is already using that special IP and/or port. So kill them:
                            $ fuser -k <code_language_port>/tcp
                            
            1.3) Check the result on the browser:
                http://<server_ip_or_domain>:<code_language_port>
                    E.g.
                        http://vps666.clound.net:5000
                
            1.4) After testing, on VPS terminal, stop to run the WSGI (ctrl+c), and deactivate the current venv!
                
            1.5) Create the service file to automating the WSGI startup on server:

                # Creating the file:
                    $ nano /etc/systemd/system/<simplified_app_name>.service
                    
                        BE AWARE:
                            This "simplified_app_name" will be used again later!
                        
                        Service file content:
                            [Unit]
                            Description=Gunicorn instance to serve <app_name>
                            After=network.target

                            [Service]
                            User=<admin_user>
                            Group=www-data
                            WorkingDirectory=/var/www/<app_folder_name>
                            EnvironmentFile=/etc/environment
                            Environment="PATH=/var/www/<app_folder_name>/venv/bin"
                            
                                >> Line for UV users:
                                    ExecStart=/home/<admin_user>/.local/bin/uv run gunicorn --bind 0.0.0.0:<code_language_port> wsgi:app
                                >> Or line for non-UV users:
                                    ExecStart=/home/<admin_user>/.local/bin/.venv/bin/gunicorn --bind 0.0.0.0:<code_language_port> wsgi:app
                                    
                            Restart=on-failure

                            [Install]
                            WantedBy=multi-user.target
                
                # Reload systemd and enable the service:
                    $ sudo systemctl daemon-reload
                    $ sudo systemctl enable <simplified_app_name>
                    $ sudo systemctl start <simplified_app_name>
                
                # Check the status:
                    $ systemctl status <simplified_app_name>
                        # You should see active (running)!
                            
                        # Do you need to change something in <simplified_app_name>.service file?
                        # Do it and, then, restart the service:
                            $ systemctl daemon-reload
                            $ systemctl restart <simplified_app_name>
                            $ systemctl status <simplified_app_name>
                            
                # Restart the VPS and check if the new service is running:
                    $ sudo reboot
                        # And after the reboot time and reconnection:
                            $ systemctl status <simplified_app_name>
                
    
    2) Configuring Nginx as a reverse proxy:
        Lets make the traffic to hit port 80 (and later 443) and to get forwarded to Gunicorn on code language port (e.g. 5000 for Python).
                
        2.PRE.1) Assuming you know this VPS IP;
        
        2.PRE.2) Assuming you know this APP official URL;
            
        2.1) Create/Open the file:
            $ sudo nano /etc/nginx/sites-available/<simplified_app_name>
        
                # The file content:
                    server {
                        listen 80;
                        # Avoid protocols (http) and 'www':
                        server_name <app_official_url>;

                        location / {
                            proxy_pass http://127.0.0.1:<code_language_port>;
                            proxy_set_header Host $host;
                            proxy_set_header X-Real-IP $remote_addr;
                            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                            proxy_set_header X-Forwarded-Proto $scheme;
                        }

                        location /static/ {
                            alias /var/www/<app_folder>/static/;
                            expires <days_you_want_to_set>d;
                            add_header Cache-Control "public, no-transform";
                        }
                    }
                    
                E.g.
                    server {
                        listen 80;
                        server_name my.portfolio.com;

                        location / {
                            proxy_pass http://127.0.0.1:5000;
                            proxy_set_header Host $host;
                            proxy_set_header X-Real-IP $remote_addr;
                            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                            proxy_set_header X-Forwarded-Proto $scheme;
                        }

                        location /static/ {
                            alias /var/www/portfolio/static/;
                            expires 30d;
                            add_header Cache-Control "public, no-transform";
                        }
                    }
                    
        2.2) Enable the app:
            $ sudo ln -s /etc/nginx/sites-available/<simplified_app_name> /etc/nginx/sites-enabled/
            
        2.3) Disable the default Nginx site:
            $ sudo rm /etc/nginx/sites-enabled/default
            
        2.4) Test and reload Nginx:
            $ sudo nginx -t
                # Output must be: "syntax is ok"
                
            $ sudo systemctl reload nginx
            
    
    3) DNS settings: 
        
        3.PRE) Assuming you got the app official domain!
    
        3.1) Go to your domain/DNS provider (of your app's official URL) and add this record:
            
            Type   -   Name   -   Value     -   TTL*
            A      -   dev    -   <VPS.IP>  -   300 (or lowest available)
            
            (*) Setting to 300 seconds (5 min) speeds up propagation for now. You can raise it later!!!
            
        3.2) Once added, monitor propagation through your browser:
            # Check with non-securite-protocol:
                http://<your-official-app-domain>
                
        3.3) After positive result, edit the DNS entry's TTL to 1800 (RECOMMENDED)!
    
        
    4) Secure Protocol configuration (HTTPS):
        /vault/web-development/domain/ssl-certification.md
        
        
        
    DONE!


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

HOW TO UPDATE YOUR APP:
    /vault/server/os/linux/updating-web-application-via-git.md