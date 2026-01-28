

VERSIONING > GIT: REMOTE

    Manages the set of remote repositories your local repository tracks.


    >> Publishing your changes (from Local Repo) to the REMOTE same branch:
        
        $ git push

        # or through remote command:

        $ git remote add origin https://github.com/<organization-name>/<project_name>.git
        $ git branch -M main (or the name of the right branch to use)
        $ git push -u origin main (or the name of the right branch to do it)