from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    db_url: str

    class Config:
        env_file = "./env/.env"
        env_file_encoding = "utf-8"


settings = Settings()