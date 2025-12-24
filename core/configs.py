from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Settings(BaseSettings):
    API_V1_STR: str = ""
    DB_URL: str = ""

    DBBaseModel: ClassVar = Base

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()
