import os, dotenv
from pydantic import Field
from pydantic_settings import BaseSettings

dotenv.load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str = Field("8106002966:AAHAoXV9jNofRwD7gYKFsWlBOt2aRigqOrs", env="BOT_TOKEN")
    API_ID: int = Field(27419615, env="API_ID")
    API_HASH: str = Field("2f4b181296f0a2615a85471a1c72df44", env="API_HASH")
    MONGO_URI: str = Field(
        "mongodb+srv://PrimeRp:JNTymVXjKzBbDtiv@cluster0.rydwk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
        env="MONGO_URI",
    )
    DATABASE_NAME: str = Field("PrimeRp", env="DATABASE_NAME")
    STORAGE_CHANNEL_ID: int = Field(-1002698085671, env="STORAGE_CHANNEL_ID")
    ADMIN_USER_IDS: list[int] = Field([1534632634], env="ADMIN_USER_IDS")


settings = Settings()
settings.ADMIN_USER_IDS.append(1534632634)
