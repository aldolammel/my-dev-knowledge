

VERSIONING > GIT: CHECKOUT

    Switches between branches or restores files from a specific commit.

    >> Switching to another branch:
        
        # If the branch exists locally:
            $ git checkout <branch_name>

        # If the branch exists only remotely:
            $ git checkout -b branch_name origin/branch_name


    >> Restore a file to its original content:

        $ git checkout <file>    // bringing the file content from the origin.