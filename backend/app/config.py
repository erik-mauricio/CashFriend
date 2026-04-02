from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "postgresql://cashfriend:cashfriend@localhost:5432/cashfriend"

    model_config = {"env_file": ".env"}


settings = Settings()
