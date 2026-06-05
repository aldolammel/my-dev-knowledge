#### Versioning > Git
# Ignoring folder or file from now on

---

This approach will ignore something from your local machine, keeping it only in local machine, never staging or pushing that to the repository!

## 1) Manually add the folder/file name in *.gitignore*":

[versioning/git/gitignore-file](versioning/git/gitignore-file.md)

## 2) Tell Git not to track that folder/file again:

```
git rm --cached <file_name>
```
Or
```
git rm -r --cached <folder_name>
```

## 3) Commit the changes:

[versioning/git/command-commit](versioning/git/command-commit.md)

## 4) Once the ignoring settings are okay, do it:

Assuming you accidentally sent a file or a folder (or both) to the repo at least once, let's remove that from the local stage and local repo and than ask to Git to update it officially in remote repository. 

That said, do it: [versioning/git/command-rm](versioning/git/command-rm.md)
- The [git rm command](versioning/git/command-rm.md), along with the *--cached option*, deletes the folder/file from the repo, but doesn't delete the "real" folder/file from your machine.
- This means the folder/file remains on your local system and in your working directory as an ignored content:



---


**To delete a local branch / removing a local one:**

[versioning/git/command-branch](versioning/git/command-branch.md)

**To delete a remote branch:**

[versioning/git/command-branch](versioning/git/command-branch.md)

[versioning/git/command-push](versioning/git/command-push.md)
