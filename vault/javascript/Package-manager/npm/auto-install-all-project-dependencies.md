NPM: MAKING AUTO INSTALLATION OF ALL PROJECT'S DEPENDENCIES

    Make Node read to front-end's 'package.json' file and install automatically all dependencies and Dev dependencies listed in there (by consequence, creating the 'node_modules' folder case it doesn't exist yet):
                
        $ npm install
                
        # Check what is installed:
            
            # Local dependencies, so in a specific project folder:
                $ npm list

            # Global dependencies, anywhere:
                $ npm list -g