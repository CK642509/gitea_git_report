from pydantic_settings import BaseSettings
from pathlib import Path

class AppConfigs(BaseSettings):
    GITEA_USERNAME: str
    GITEA_PASSWORD: str

    class Config:
        env_file = ".env"

if __name__ == '__main__':
    settings = AppConfigs()
    print(settings)
    print(settings.GITEA_USERNAME)
    print(settings.GITEA_PASSWORD)