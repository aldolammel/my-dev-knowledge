#### Versioning > Git > Command
# Merge

---

Combines changes from one branch into your current branch.

Alternatives to merging: [/versioning/git/command-fetch](/versioning/git/command-fetch.md)

---
## Merging two branches:

**Make a decision:**
- A) If NOT new stuff in the main branch
- B) If there's new stuff in the main branch

......................................

### A) if NO new stuff in the main branch
Given that you're the sole developer and no changes have been made to main since you branched off to the other branch you have been working, merging is straightforward and safe approach:

A1) Switch to "main" branch:
```bash
git checkout main
```

A2) Merge that "working branch" (that one with new approaches/fixes) into main:
```bash
git merge branch_name_here
```

A3) Commit it:
```bash
git commit -m 'Merged XXXXX with main'
```

A4) CRITICAL: Test the main branch!

A5) (If applicable) In case you wanna delete:
- Local branch: [/versioning/git/command-branch](/versioning/git/command-branch)

A6) Do you want to keep the working branch active for future development work?

A6A) Keep it:
```bash
# Switch back to working branch to continue working:
git checkout branch_name_here
```
                
A6B) Or delete it:
```bash
git branch -d branch_name_here  # local deletion
git push origin --delete branch_name_here  # remote deletion
```

......................................

### B) if there's new stuff in the main branch
B1) Update your local main branch first:
```bash
git checkout main
git pull origin main
```

B2) CRITICAL: Always locally, merge main into the "working branch" (that one with new approaches/fixes) to resolve any conflicts:
```bash
git checkout branch_name_here
git merge main
```
Resolve any conflicts if they occur!
CRUCIAL: Test thoroughly after merging!

B3) After testing, merge working branch into main:
```bash
git checkout main
git merge branch_name_here
git push origin main
```

---




