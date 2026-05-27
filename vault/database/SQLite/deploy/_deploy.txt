

SQLITE: DEPLOYING


    1) Where should your db be installed:
        
            1A) xxxxxxxxxxxxxxxxxx
            1B) Within the project folder (NOT RECOMMENDED FOR SENSITIVE DATA)
            
            - - - - -
            
            1A) xxxxxxxxxxxxxxxxxxxxx - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
                xxxxxxxxxxxxxx
                
            1B) DB within the project folder - - - - - - - - - - - - - - - - - - - - - - - - - - - -
            
                1B.1) In your local machine:
                    
                    1B.1.1) Make sure your .gitignore won't block the db to be upload to the repo;
                        E.g.
                            #db.sqlite3
                            #db.sqlite3-journal
                
                    1B.1.2) Still in the local environment, push the changes on git!
                        /vault/versioning/git/command-push.txt
                
                1B.2) In the server machine:
                    
                    1B.2.PRE) Assuming you're in the right project folder, and using the right venv!
                    
                    1B.2.1) Update the app from repo:
                        /vault/versioning/git/command-pull.txt
                        
                    1B.2.2) Check if db file is in the right place. If not, check again your .gitignore file!
                    
            - - - - -
            
            
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 