

VERSIONING > GIT: RM

    Removes files from both the working directory and the staging area (marks them for deletion in the next commit).


    >> Deleting a file (from local machine and repository):
        
        $ git rm <file>
        $ git status                          // only to check what's ready for the stage.
        $ git commit -m "removed useless file"
        $ git push


    >> Deleting a folder (from local machine and repository):

        $ git rm -r <folder>
        $ git status                          // only to check what's ready for the stage.
        $ git commit -m "removed useless folder"
        $ git push

    
    >> Deleting a file (only from repository):

            $ git rm --cached <full_file_name>
            $ git commit -m "removed useless file only from repo"
        
        >> Now, make sure you updated .gitignore file with the file to avoid!

            # Update the repo:
                $ git push


    >> Deleting a folder (only from repository):

            $ git rm -r --cached <full_folder_name>
            $ git commit -m "removed useless folder only from repo"
        
        >> Now, make sure you updated .gitignore file with the folder to avoid!
        
            # Update the repo:
                $ git push


    >> Deleting a local branch:

        ./command-branch.txt


    >> Deleting a remote branch (using push):

        ./command-push.txt


    >> Deleting the local repository:
        # delete the .git folder,
        # or inside the project folder, do it:
            $ rm -rf .git