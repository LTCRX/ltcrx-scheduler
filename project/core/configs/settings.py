import os
from pathlib import Path
from dotenv import load_dotenv


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "LTC-RX Scheduller"
    PROJECT_VERSION: str = "0.0.1"
    ROOT_PATH: str = os.getenv("ROOT_PATH", "")


settings = Settings()
