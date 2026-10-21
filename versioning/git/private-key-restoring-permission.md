(THIS IS JUST A SCRATCH ---------------------------------)

#### Versioning > Git
# Restoring Git permission in your project environment

---
## Before:
1. Assuming you are in the right project folder root.

---
## Creating your SSH Key:

Check if an SSH key exists on your server:
```bash
ls -la ~/.ssh
```

Generate a new SSH key and add it to GitHub:
```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```
then:
1. "Enter file in which to save the key (/root/.ssh/id_ed25519):" press ENTER
2. And define a password/passphrase.

Run this command and copy the output result:
```bash
cat ~/.ssh/id_ed25519.pub
# Output example: ssh-ed553419 AAVSSdC3NzaC1lCDI1NTE5AAAAIASFFv+cIAtpWDw3qzNF7rjSJ4go/UOkoghDDMa1qQ rockbalboa@hotmail.com

```

Add that output result to: GitHub -> Settings -> SSH and GPG keys, add a SSH KEY (not GPG one), and run:
```bash
ssh -T git@github.com
# and provide your password/passphrase!
```

Done!