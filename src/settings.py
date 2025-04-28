from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the application.
    """

    # General settings
    OPEN_AI_API_KEY: str


settings = Settings()
