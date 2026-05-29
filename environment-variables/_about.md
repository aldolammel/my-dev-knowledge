ENVIRONMENT VARIABLES:

    Those variables linked exclusively with the environment where the code is running. It's a safe option to save keys, passwords, tokens and other information that must be unique for each environment.


        >> Web-development:

            For those projects that back-end and front-end have different solutions, each one has its own environment. That said, for that cases expect 2 environment files for the same project. Each file with its environment variables: sometimes with duplicated vars, sometimes with unique vars.

            No matter what, .env files are used ONLY for development/staging environments, NEVER for production environments! For production, unlike for development/staging, the project's environment variables are registered directly in the VPS operational system!

---

    Examples of .env:
        /environment-variables/
