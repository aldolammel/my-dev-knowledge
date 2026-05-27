

WEB-SERVER > NGINX: INSTALLING

    
    Nginx is a system-level service, so it must be installed always globally in the OS!
    
    
    PRE.1) What is it:
        ./_about.md
      
        
    1) Install it:
    
        1.PRE) Assuming you are NOT activated on any venv!
        
        1.1) Installing:
            
            >> Debian/Ubuntu:
                $ sudo apt install -y nginx
            
            >> Windows:
                $ xxxxxxxxxxxxxxxx
            
            >> Mac:
                $ xxxxxxxxxxxxxxxx
                
    
    2) Integration:
    
        2.1) (If applicable) Include the Nginx service in your current firewall rules!
        
        2.2) Test it:
        
            >> Debian/Ubuntu:
                $ sudo systemctl enable nginx
                $ sudo systemctl start nginx
                $ sudo systemctl status nginx
                
            >> Windows:
                $ xxxxxxxxxxxx
        