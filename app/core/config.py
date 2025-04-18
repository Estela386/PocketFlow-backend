import os

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    API_VERSION = "1.0"

settings = Settings()
