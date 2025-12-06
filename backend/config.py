from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    app_name: str = Field("Green Hearing AI Platform", env="APP_NAME")
    database_user: str = Field("postgres", env="DATABASE_USER")
    database_password: str = Field("password", env="DATABASE_PASSWORD")
    database_host: str = Field("localhost", env="DATABASE_HOST")
    database_port: int = Field(5432, env="DATABASE_PORT")
    database_name: str = Field("app_db", env="DATABASE_NAME")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

    @property
    def database_url(self) -> str:
        """Construct the PostgreSQL connection URL."""
        return (
            "postgresql+psycopg2://"
            f"{self.database_user}:{self.database_password}"
            f"@{self.database_host}:{self.database_port}/{self.database_name}"
        )


def get_settings() -> Settings:
    """Return cached settings instance."""
    return Settings()
