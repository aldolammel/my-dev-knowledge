

DATABASE > SQLITE: INSTALLATION

    
    PRE.1) Make sure you are in the right virtual environment!
    
    
    PRE.2) For Python projects:
    
        SQLite3 is part of Python's standard library, it comes with Python itself.
        
        >> How do you installed your Python?
            
            PRE.2A) It came with the OS/distro;
            PRE.2B) I've installed it using a built-in Linux/distro package manager;
            PRE.2C) I've installed it using UV;
            
            - - - - - 
            
            PRE.2A) Came already installed with the OS/distro - - - - - - - - - - - - - - - - - - - 
                $ python -c "import sqlite3; print(sqlite3.sqlite_version)"
            
            PRE.2B) I've used a built-in package manager - - - - - - - - - - - - - - - - - - - - - -
                Same approach as "A";
            
            PRE.2C) I've used UV - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                
                PRE.2C.1) Make sure you already activated the project venv;
                
                PRE.2C.2) Same approach as "A";
        
    
    1) (If applicable)
        If no SQLite yet or if you need a standalone SQLite3 CLI tool (to inspect .db files from the terminal), you could install it at the OS level:
        
            $ sudo apt install -y sqlite3
        
                # Check if not installed yet:
                    $ sqlite3 --version
        
        
    2) Integration:
        xxxxxxxxxxxxxxx