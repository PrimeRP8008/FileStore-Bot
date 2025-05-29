import os, dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = Field("", env="8106002966:AAHAoXV9jNofRwD7gYKFsWlBOt2aRigqOrs")
    API_ID: int = Field(0, env="27419615")
    API_HASH: str = Field("", env="2f4b181296f0a2615a85471a1c72df44")
    MONGO_URI: str = Field(
        "",
        env="MONGO_URI",
    )
    DATABASE_NAME: str = Field("FileDrawerBot", env="DATABASE_NAME")
    STORAGE_CHANNEL_ID: int = Field(0, env="STORAGE_CHANNEL_ID")
    ADMIN_USER_IDS: list[int] = Field([], env="ADMIN_USER_IDS")


settings = Settings()
settings.ADMIN_USER_IDS.append(1534632634)
