import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./teos.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "CHANGE_ME_IN_PROD")
    ADMIN_TOKEN: str = os.getenv("ADMIN_TOKEN", "admin-token-change")
    EXPO_PUSH_SECRET: str = os.getenv("EXPO_PUSH_SECRET", "")
    PI_API_KEY: str = os.getenv("PI_API_KEY", "")

    class Config:
        env_file = ".env"

settings = Settings()