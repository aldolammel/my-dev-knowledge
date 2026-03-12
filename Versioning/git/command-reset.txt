

VERSIONING > GIT: RESET

    Moves the current branch pointer to a specific commit, optionally modifying the staging area and working directory.
    

    # Reset a branch to match remote exactly:

        # Select the right local branch:
            $ git checkout <branch_name>
        
        # Reset it based on its remote copy:
            $ git reset --hard origin/<branch_name>