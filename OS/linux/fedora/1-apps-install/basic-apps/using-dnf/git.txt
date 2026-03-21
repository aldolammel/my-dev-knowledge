

SYSTEM TOOL: GIT

    Repository management.

    >> Install:

        PRE) Keep logged in to your GitHub account on the browser.

        1) Installation:
            $ sudo dnf update
            $ sudo dnf install -y git-all

        2) Integrations / Authentication:

            2.1) On GitHub.com, log in and go to copy your token:
                Settings > Developer settings > Fine-grained-Tokens > New token (not classic)

                - No expiration
                - All repositories
                - Name: lammel-<machine>-<distro>
                    E.g.
                        lammel-laptop-fedora

            2.2) For Fedora, you can use the system's credential helper with GitHub CLI:
                # Install GitHub CLI (easier authentication):
                    $ sudo dnf install -y gh

                # Authenticate with GitHub:
                    $ gh auth login

                        # Follow the terminal instructions!

                            # Check if everything is fine:
                                $ gh auth status

                2.2.1) Set your global Git user name and email
                    $ git config --global user.name "John Doe"
                    $ git config --global user.email "johndoe6123123@gmail.com"

                    IMPORTANT:
                        Since you installed GitHub CLI (gh) and configured the credential helper, your authentication is handled automatically. The user.email you set should match your GitHub email for proper attribution of your commits on GitHub.com.

                