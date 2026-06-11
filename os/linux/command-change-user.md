#### OS > Linux

# Switching the system user on terminal

Figure out the current user on the system:
```
whoami
```
This is the way for the most Linux distros!
```
sudo -i -u <user_name>
```
E.g. changing the *lammelaldo* user to *postgres* user:
```
sudo -i -u postgres
```

**Before running the command:**
lammelaldo@ubuntu-desk:~$

**After running the command:**
postgres@ubuntu-desk:~$
