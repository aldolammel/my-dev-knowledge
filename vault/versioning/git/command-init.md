

VERSIONING > GIT: INIT

    Initializes a new Git repository in the current directory.


    >> Creating a new repository (by terminal):
            
        # Creating the project folder:
            $ mkdir <project-name>

        # Copy the .gitignore file to the project folder root:
            ./.gitignore
        
        # In the project folder:

            # Initialize Git versioning for this folder:
                $ git init
            
            # Telling git this project has something to versioning:
                $ git add --all
                $ git commit -m "first commit"
            
            # Defining which branch the versioning will work now:
                $ git branch -M main
            
            # (if applicable) Install the gh dependency:
                $ sudo apt install -y gh
                
                # Authenticate the dependency:
                    $ gh auth login
                        
                        1) GitHub.com
                        2) HTTPS
                        3) GitHub Credentials
                        4) Login with a web browser
                        5) Copy the pre-code validation
                        6) Use the 2-factor to validate!
                        7) Done!

            # Create the remote repository on GitHub:
                $ gh repo create abcoo-ideias/<project_simpler_name> --private
            # Connect the new remote repo to the local one:
                $ git remote add origin https://github.com/abcoo-ideias/<project_simpler_name>.git
                $ git push -u origin main