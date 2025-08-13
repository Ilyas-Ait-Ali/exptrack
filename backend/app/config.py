from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite+aiosqlite:///./exptrack.db" 
    CORS_ORIGINS: str = "*"  

settings = Settings()
