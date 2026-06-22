#### Versioning > Git
# Basic about Git

---

It's a version system to control project files version.
## Git workflow:
1. Local > You develop something locally;
2. Local > Send it to local stage area (git add);
3. Local > Send it to local repo (git commit);
4. Remote > Send it to remote repo (git push);
5. Merge or not the main branch.
## Installing:

**Before:**
1. Assuming you're NOT in a project venv!

**1) Install it globally (recommended)**
```
sudo apt install -y git
```

---
## What do you want from:

### Creating/Cloning
- Creating a new repo: [/versioning/git/command-init](/versioning/git/command-init.md)
- Creating a new local branch: [/versioning/git/command-branch](/versioning/git/command-branch.md)
- Creating a new remote branch: [/versioning/git/command-push](/versioning/git/command-push.md)
- Getting in/Cloning an existent project/repo: [/versioning/git/command-clone](/versioning/git/command-clone.md)
### Checking/Switching
- Checking which branch you are: [/versioning/git/command-branch](/versioning/git/command-branch.md)
- Switching to another branch: [/versioning/git/command-checkout](/versioning/git/command-checkout.md)
- Checking if you have the last version of the main branch: 
	- A report with all commits: [/versioning/git/command-log](/versioning/git/command-log.md)
	- Find all changes without merging these changes into your current working branch: [/versioning/git/command-fetch](/versioning/git/command-fetch.md)
	- OR pull it, fetching and merging (or rebases) changes: [/versioning/git/command-pull](/versioning/git/command-pull.md)
### Adding/Merging/Updating
- Put a specific file/change on LOCAL stage: [/versioning/git/command-add](/versioning/git/command-add.md)
- Stages all your changes in the entire working folder, including modifications, new files, and deletions: [/versioning/git/command-add](/versioning/git/command-add.md)
- Stages your changes in the current folder and its sub-folders, but NOT including deletions: [/versioning/git/command-add](/versioning/git/command-add.md)
- Sending your changes to the LOCAL repo: [/versioning/git/command-commit](/versioning/git/command-commit.md)
- Taking updates from teammates to the REMOTE same branch: [/versioning/git/command-pull](/versioning/git/command-pull.md)
- Merging two branches: [/versioning/git/command-merge](/versioning/git/command-merge.md)
- Publishing your changes (from LOCAL repo) to the REMOTE same branch:
	- [/versioning/git/command-push](/versioning/git/command-push.md)
	- Or through remote command: [/versioning/git/command-remote](/versioning/git/command-remote.md)
### Restoring/Fixing
- Restore a file to its original content: [/versioning/git/command-checkout](/versioning/git/command-checkout.md)
- Force the original branch again: [/versioning/git/command-reset](/versioning/git/command-reset.md)
- Ignoring a folder or file from now on: [/versioning/git/ignoring-folder-or-file-from-now-on](/versioning/git/ignoring-folder-or-file-from-now-on.md)
### Deleting
- Deleting a file (from local machine and repo): [/versioning/git/command-rm](/versioning/git/command-rm.md)
- Deleting a folder (from local machine and repo): [/versioning/git/command-rm](/versioning/git/command-rm.md)
- Deleting a file (only from repo): [/versioning/git/command-rm](/versioning/git/command-rm.md)
- Deleting a folder (only from repo): [/versioning/git/command-rm](/versioning/git/command-rm.md)
- Deleting a local branch: [/versioning/git/command-branch](/versioning/git/command-branch.md)
- Deleting a remote branch (using push): [/versioning/git/command-push](/versioning/git/command-push.md)
- Deleting the local repo:
	-  Delete the .git folder;
	-  Or inside the project folder, use this command: [/versioning/git/command-rm](/versioning/git/command-rm.md)

---
