"""

ENVIRONMENT VARIABLES:
Those variables linked exclusively with the environment where the code is running. It's a safe option to save
keys, passwords, tokens and other information that must be unique for each environment.

There is two ways to set environment variables:

1) Through the IDE:
    Important: The process changes according the IDE you're using. This way isn't possible on some IDE's like Jupyter.
    Go to "Edit configurations" of your py-file and in "Environment variables" edit them including what you need.
    After that, call the lines down below, for example, if you're including user and password as env-variables:
        import os
        user = os.environ["user"]
        pass = os.environ["password"]


2) Through a file:
    Create a file called ".env" on the project root and call the both lines down below:
        from dotenv import load_dotenv
        load_dotenv()


Crucial: an environment variable just exist for each file that was created. It's NOT global.


"""
# USING THE METHOD "THROUGH THE IDE":

# responsible to call all environment variables:
import os
# Calling the secret token from environment variable list:
PROTECTED_TOKEN = os.environ["TOKEN"]
# checking:
print(f"Token loaded on this environment: {PROTECTED_TOKEN}")
print(f"All environment variables loaded here: {os.environ}")
