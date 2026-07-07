#### Versioning > Git
# Command: rm

---

Removes files from both the working directory and the staging area (marks them for deletion in the next commit).

---
## Deleting a file:

- From local machine and repository;
- Or only from local machine;
- Or only from repository;

**From local machine and repository:**
```
git rm <path-from-project-root-to-folder>
git status                          // only to check what's ready for the stage.
git commit -m "removed useless file"
git push
```

**Only from local machine:**
Just delete the file in your favorite way!

**Only from repository:**
```
git rm --cached <path-from-project-root-to-file>
git commit -m "removed useless file only from repo"
```
Update the repo - Now, make sure you updated .gitignore file with the file to avoid:
```
git push
```

---
## Deleting a folder:

- From local machine and repository;
- Or only from local machine;
- Or only from repository;

**From local machine and repository:**
```
git rm -r <path-from-project-root-to-folder>
git status                          // only to check what's ready for the stage.
git commit -m "removed useless folder"
git push
```

**Only from local machine:**
Just delete the folder in your favorite way!

**Only from repository:**
```
git rm -r --cached <path-from-project-root-to-folder>
git commit -m "removed useless folder only from repo"
```
Update the repo - Now, make sure you updated .gitignore file with the folder to avoid:
```
git push
```

---
## Deleting a local branch:

[/versioning/git/command-branch](/versioning/git/command-branch.md)

---
## Deleting a remote branch (using push):

[/versioning/git/command-push](/versioning/git/command-push.md)

---
## Deleting the local repository:
Delete the .git folder or inside the project folder, do it!
```
rm -rf .git
```

---
