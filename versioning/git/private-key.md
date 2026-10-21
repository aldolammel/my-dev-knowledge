#### Versioning > Git
# Create a Private Key for GitHub/GitLab access to the server

---

==IMPORTANT:==
This is NOT to create a **Public Key** to replace the SSH connection password!

---

## Which type of key you want:

>> Ed25519:
A more modern algorithm with a smaller standard key size of 256 bits. It is just as secure and efficient as an RSA key due to its strong cryptographic properties. The compatibility is lower, but newer operating systems support it.

>> RSA:
An SSH RSA key is considered highly secure as it has typically larger key sizes, often 2048 or 4096 bits. It's also more compatible with older OS.

        7.PRE) Assuming you're in VPS terminal!

        7.1) Generate the key:
            >> Using an Ed25519 (GitHub recommended standard, 2026):
                $ ssh-keygen -t ed25519 -C "<admin_user_here>@<vps_name_here>"
                    E.g.
                        $ ssh-keygen -t ed25519 -C "ayrtonsenna@vps666"

            >> Or using an RSA:
                $ xxxxxxxxxxxxxxxxxxxxxxx
                    E.g.
                        $ xxxxxxxxxxxxxxxxxxxxxxxxxxxx

        7.2) After that, the key generator should ask you to choose a location to store the keys. Just press ENTER to confirm the key location on VPS!
            E.g.
                /home/<your_user>/.ssh/id_ed25519
                Or
                /home/<your_user>/.ssh/id_rsa

        7.3) The key generator window will ask you to create an SSH key passphrase to access your private key. Set the same admin user password OR use Norton Generated Password to create it:
            https://us.norton.com/feature/password-generator

            INFO:
                This pass you will used when you GIT CLONE the app repo in production, for example!

        7.4) Once the key is created, ignore all the terminal output and just copy and save what the terminal prints here:
            >> Using Ed25519:
                $ cat ~/.ssh/id_ed25519.pub
            >> Using RSA:
                $ cat ~/.ssh/id_rsa.pub

---

## 8) Prepare the server to receive clones from GitHub repositories:

        8.1) On GitHub, go to:

            >> Settings >> SSH and GPG Keys >> New SSH Key;

                Title example = <vps_name>-<vps_username>
                    e.g. vps666-kornuser

                Key type = Auth Key

                Key = Set here the key you previously saved (step 7.4)

                And then "Add SSH key"!
                Now you are prepared to clone private GitHub repos into the server.

        8.2) On the VPS terminal, test it:
            $ ssh -T git@github.com

                Output e.g.
                    The authenticity of host 'github.com (1.111.11.111)' can't be established.
                    ED25519 key fingerprint is xyxyxyxyxyxyxyxyxyxyxyxy.
                    This key is not known by any other names.
                    Are you sure you want to continue connecting (yes/no/[fingerprint])?

                # Say "yes" for the very first connection!

                    # Confirm with your Private Key password and done!

        8.3) Install Git globally on VPS:
[/versioning/git/\_basic](/versioning/git/_basic.md)

            
---
## Restoring your existing permission:
[versioning/git/private-key-restoring-permission](versioning/git/private-key-restoring-permission.md)

