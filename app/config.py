from dotenv import load_dotenv
import os

load_dotenv()
FIREBASE_CREDENTIALS_PATH = os.getenv("FIREBASE_CREDENTIALS_PATH")
CLIMATIQ_API_KEY = os.getenv("CLIMATIQ_API_KEY")
CLIMATIQ_API_URL = "https://beta3.api.climatiq.io"