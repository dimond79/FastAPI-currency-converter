from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    EXCHANGE_API_KEY: str
    EXCHANGE_API_URL: str

    class Config:
        env_file =".env"

settings = Settings()