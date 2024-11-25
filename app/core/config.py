from dotenv import load_dotenv
from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent

load_dotenv()


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "core" / "certs" / "private_key.pem"
    public_key_path: Path = BASE_DIR / "core" / "certs" / "public_key.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    auth_jwt: AuthJWT = AuthJWT()
    DBAPI: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
