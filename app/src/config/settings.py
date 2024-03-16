import os

from app.src.utils.constants import BASE_DIR
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = os.getenv("APP_ENV", "test")
    database_port: int = int(os.getenv("DATABASE_PORT", 5432))
    database_password: str = os.getenv("DATABASE_PASSWORD", "password")
    database_user: str = os.getenv("DATABASE_USER", "user")
    database_db: str = os.getenv("DATABASE_DB", "db")
    database_host: str = os.getenv("DATABASE_HOST", "localhost")
    api_prefix: str = os.getenv("API_PREFIX", "/api/v1")
    project_name: str = os.getenv("PROJECT_NAME", "Escape Room")
    backend_cors_origins: str = os.getenv("BACKEND_CORS_ORIGINS", "*")

    @property
    def backend_cors_origins_list(self) -> list[str]:
        return [origin.strip() for origin in self.backend_cors_origins.split(",")]

    logging_config_file: str = os.getenv("LOGGING_CONFIG_FILE", "logging.conf")
    project_version: str = os.getenv("PROJECT_VERSION", "0.0.1")

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()
