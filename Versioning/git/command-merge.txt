

VERSIONING > GIT: MERGE

    Combines changes from one branch into your current branch.

    Alternatives to merging?
        ./command-fetch.txt



    >> Merging two branches:

        >> Approach A: if NO new stuff in the main branch - - - - - - - - - - - - - - - - - - - - - 
            
            Given that you're the sole developer and no changes have been made to main since you branched off to the other branch you have been working, merging is straightforward and safe approach:

            1. Switch to "main" branch:
                $ git checkout main

            2. Merge that "working branch" (that one with new approaches/fixes) into main:
                $ git merge <branch_name>

            3. Push to remote:
                $ git push origin main
                    # It's expected the prompt to return "Total 0, reused 0, pack-reused 0".

            4. CRITICAL: Test the main branch!

            5. Do you want to keep the working branch active for future development work?

                5A) Keep it:

                    # Switch back to working branch to continue working:
                    $ git checkout <branch_name>
                
                5B) Or delete it:
                    
                    $ git branch -d <branch_name>  # local deletion
                    $ git push origin --delete <branch_name>  # remote deletion


        >> Approach B: if there's new stuff in the main branch - - - - - - - - - - - - - - - - - - -

            1. Update your local main branch first:
                $ git checkout main
                $ git pull origin main

            2. CRITICAL: Always locally, merge main into the "working branch" (that one with new approaches/fixes) to resolve any conflicts:

                $ git checkout <branch_name>
                $ git merge main

                # Resolve any conflicts if they occur!
                # CRUCIAL: Test thoroughly after merging!

            3. After testing, merge working branch into main:
                $ git checkout main
                $ git merge <branch_name>
                $ git push origin main