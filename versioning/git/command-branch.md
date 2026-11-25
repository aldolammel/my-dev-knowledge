#### Versioning > Git > Command
# Branch

---

Lists, creates, or deletes branches in your repository.

---
## Before:

**Checking which branch you are:**

Check local branch:
```bash
git branch
```
Check all branches available, including local:
```bash
git branch -a
```

---
## 1) Creating a new local branch:
        
1.1) Creating it:
```bash
git branch new_branch_name
```

1.2) Selecting it:
```bash
git checkout new_branch_name
```

1.3) (If applicable) Create it as remote too (using push): [/versioning/git/command-push](/versioning/git/command-push.md)

---
## Deleting a local branch:
```bash
git branch -d branch_name_here
```
## Force the original branch again:
[/versioning/git/command-reset](/versioning/git/command-reset.md)
## Deleting a remote branch (using push):
[/versioning/git/command-push](/versioning/git/command-push.md)

