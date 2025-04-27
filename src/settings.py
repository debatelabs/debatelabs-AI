from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    """
    Settings for the application.
    """

    # General settings
    OPEN_AI_API_KEY: str 

    TEMP_PATH: Path = Path("src/temp")


settings = Settings()