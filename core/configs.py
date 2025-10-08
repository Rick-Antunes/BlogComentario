from typing import ClassVar

from typing import List

from sqlalchemy.ext.declarative import declarative_base

from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    API_V1: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://postgres:123@localhost:5432/blog"
    DBBaseModel: ClassVar = declarative_base()
<<<<<<< HEAD
    
    class config:
        case_sensitive = True

settings = Settings()
=======

    JWT_SECRET: str = 'PqG0RxyEZKPspN5gIIzyHUVqIxroEcGvghd6WH78-Mk'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class config:
        case_sensitive = True

settings: Settings = Settings()
>>>>>>> 689446a (first commit)
