from pydantic.config import BaseSettings, Field


class Settings(BaseSettings):
    """Settings for the application."""

    # General settings
    OPEN_AI_API_KEY: str 
