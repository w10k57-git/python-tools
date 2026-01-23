"""Application configuration."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )

    app_name: str = "Mechanical Engineering API"
    api_version: str = "v1"
    debug: bool = False
    cors_origins: list[str] = ["*"]


settings = Settings()
