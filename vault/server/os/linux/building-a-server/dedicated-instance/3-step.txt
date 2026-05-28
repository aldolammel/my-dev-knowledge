

DEBIAN/UBUNTU > BUILDING UP A VPS: DEPLOYING A WEB APP


    PRE.1) Assuming you have finished the previous steps!
    
    
    PRE.2) You're in the VPS terminal!
    
    
    PRE.3) (If applicable)
        You're in as admin user, and not as root!
    
    
    1) VPS projects main folder:
    
        1.PRE) (If applicable)
            Make sure you are using the admin user and not the root one!
            
                
        1.1) Go to: 
            # This is the convention path:
                /var/www/
        
        1.2) Create the project folder:
            $ sudo mkdir <your_app_folder>
                E.g.
                    portfolio_2024
                    
        1.3) Set your admin permissions for this new folder too:
            
            1.3.PRE) Stay in /var/www;
            
            1.3.1) Adding permissions:
                $ sudo chown <admin_user>:<admin_user> /var/www/<your_app_folder>
                $ sudo chmod 755 /var/www/<your_app_folder>
                $ ls -l
                    # You wanna see your admin name side-by-side with your app folder name!
        
        KEEP IT IN MIND:
            1 - Project path: /var/www/<your_app_folder>
            2 - DON'T CREATE ANY .VENV FOLDER YET!
    
    
    2) Clone the web application (based in an existing Git repository) on prod:
        
        2.PRE.1) Assuming you're in VPS project folder now!
            E.g.
                /var/www/<your_app_folder>
        
        2.PRE.2) Assuming you DON'T create any venv folder there!
        
        2.PRE.3) Assuming you already installed GIT globally on VPS!
        
        2.PRE.4) (If applicable) Assuming you DON'T installed anything with UV yet!
        
        2.1) Clone your project repo from GitHub here:
        
            CRUCIAL:
                On GitHub, use the "SSH" hyperlink version to clone the repo. That will ask for Public Key already created!
                
            /vault/versioning/git/command-clone.txt
            
            # GitHub will ask for the Public Key password!
            
            
    3) Installing the app dependencies on VPS:

        3.1) Installing the package manager:
            >> UV (RECOMMENDED):
                # Only install it, and do nothing more by now:
                    /vault/python/package-manager/uv/
                
            >> Or PIP:
                Built-in Python solution, but the Python in Debian doesn't bundled PIP. So do it manually if needed!
                    /vault/python/package-manager/pip/
                    
        3.2) Make sure you are back in the VPS app folder!
            
        3.3) App venv creation:
            >> Using UV:
                # Skip this step because UV automatic create it through the install step (next one)!
                
            >> Or using Python-venv module:
                /vault/python/3-virtual-environment/creating-virtual-environment.txt
            
        3.4) Installing app dependencies:
            >> For UV users:
                # Sync (install) the dependencies:
                    /vault/python/package-manager/uv/auto-installation-with-sync.md
                    
                    # Make sure your already activated the app venv:
                        /vault/python/3-virtual-environment/activate-and-deactivate.txt
                        
                        # Check if all app dependencies were installed:
                            $ uv pip list
            
            >> Or for PIP users:
                # Make sure your already activated the app venv:
                    /vault/python/3-virtual-environment/activate-and-deactivate.txt
                
                    # How to auto install the app dependencies with PIP:
                        /vault/python/package-manager/pip/auto-installation-from-requirements-file.md
                        
                        # Check if all app dependencies were installed:
                            $ pip list
            

    4) Install Python, and its crucial tools:
        
        4.PRE.1) Assuming you are connected in the VPS terminal!
        
        4.PRE.2) Assuming you're using the right venv!
        
        4.1) Installing:
        
            >> For UV users:
                # Probably, after the uv sync, Python was installed! But check it out:
                    $ python3 --version
                    
                    # If you need to install or change the Python version:
                        /vault/python/package-manager/uv/install-python-with-uv.md
    
        
            >> Or for NON-UV users:
                /vault/python/1-python-installation/_install.md

    
    5) Installing the database:
    
        >> Using SQLite3 (Python bundled db solution):
            /vault/database/SQLite/0-basic/1-installing-and-integrating.md
            
        >> Using Postgresql:
            /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    
    6) WSGI installing, building the bridge between the Webserver and the app's code language:
    
        6.1) Installation:
            How do you installed the project's WSGI solution during the development phase?
        
                6.1A) Globally in my local machine;
                6.1B) Locally, in the app venv [by project] (RECOMMENDED);
                
                - - - - - 
                
                6.1A) Globally - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                
                    >> For Python projects:
                        >> Gunicorn solution:
                            /vault/server/_languages-server-tools/python/gunicorn/install.txt
                        
                
                6.1B) By project - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                    
                    6.1B.PRE) Probably you already installed during the dependency installations. But check it:
                        >> For UV users:
                            $ uv pip list
                        >> Or for PIP users:
                            $ pip list
                            
                    6.1B.1) (If applicable) If not installed yet:
                        /vault/server/_languages-server-tools/python/gunicorn/install.txt
                        
                - - - - -   
                    
        6.2) Update the firewall:
            
            PRE) Which language:
                >> For Python projects, port = 5000;
                
            6.2.1) Release the code language port:
                >> Using UFW:
                    $ sudo ufw allow <programming_language_port>
            
            6.2.2) Check firewall current rules:
                >> Using UFW:
                    $ sudo ufw status verbose
        
                    
    7) Environment variables on Production (VPS):
    
        7.1) (If applicable) Once your project is on prod, set the VPS environ vars:
            
            # Open the Env Vars list of the VPS:
                $ sudo nano /etc/environment

            # Copy the env vars from the back-end project's .env file to the VPS!
                
                ATTENTION:
                    Check if all env var values make sense to go like that to prod!
                
                CRITICAL:
                    Don't be stupid as hell to send your .env file to the repo, or even to the prod!
                
            # Save it (ctrl+s) and exit (ctrl+x).
            
            # Logout and reconnect to the VPS to check the new env vars:
                $ exit
                $ <connect again>
                $ printenv
  
    
    8) Testing the app:
    
        8.1) Preparing a testing file:
        
            # Replace your product main file for one of them below just for test if the server is printing out the product:
        
            >> For Python > Flask projects:
                /vault/python/web-development/flask/z_examples/_minimal-code.py
            
            >> For Python > Django projects:
                /xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
                
        8.2) Check if the production environment is showing the project product on browser:
        
            8.2.PRE.1) Assuming the prod environment is using a 'hello world' (minimal code) version for testing!
            
            8.2.PRE.2) Assuming you're using the right venv!
            
            8.2.1) Run the test:
                # For Python:
                    $ python3 <app_testing_main_file>.py

            8.2.2) Check on browser:
                >> For Python:
                    http://<vps_address>:5000
                    
                # Error case: the port is already in use?
                    $ ps -fA | grep python
                    
                    Output e.g.
                        root   10445   10351   0   19:20   pts/1   00:00:00 /var/www/xxxx/venv/bin/python /var/www/xxxx/venv/bin/flask run
                        The process id (pid) is the second number (10351). So if you want to use the default port (5000), stop the process that is using it:
                    
                    $ kill 10351
                        # And then try again!


- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    NEXT STEP:
        ./4-step.txt