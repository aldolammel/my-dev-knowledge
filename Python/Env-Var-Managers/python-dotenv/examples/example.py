from dotenv import load_dotenv
import os

load_dotenv()  # Loads variables from .env into the environment

secret = os.getenv('SECRET_KEY')
db_url = os.getenv('DATABASE_URL')