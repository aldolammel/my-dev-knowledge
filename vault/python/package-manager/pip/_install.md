

PIP (PYTHON BUILT-IN MODULE): INSTALLING


    Windows:
        $ py -m pip install --upgrade pip

    
    
    Debian & Ubuntu:
    
        # Just for make sure even the system apps list is updated:
            $ sudo apt update
    
        >> Specific for Ubuntu:
            Pip already comes with Python installation, so just update it!
                $ python3 -m pip install --upgrade pip
            
        >> Specific for Debian:
            Pip is not bundled with Python (even though it's the Python built-in package manager)!
                $ sudo apt install -y pip
        
        

    Mac:
        $ python3 -m pip install --upgrade pip
