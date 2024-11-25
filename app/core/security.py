import hashlib, string, random
from datetime import datetime, timedelta
import jwt

from app.core.config import settings


def get_random_string(length=12):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def hash_password(
    password: str,
    salt: str = None,
):
    if salt is None:
        salt = get_random_string()
    enc = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt.encode(),
        100_000,
    )
    return enc.hex()


def create_db_password(password):
    salt = get_random_string()
    hashed_password = hash_password(password, salt)
    new_password = f"{salt}${hashed_password}"
    return new_password


def validate_password(password: str, hashed_password: str):
    salt, hashed = hashed_password.split("$")
    return hash_password(password, salt) == hashed


def encode_jwt(
    payload: dict,
    private_key: str = settings.auth_jwt.private_key_path.read_text(),
    expire_minutes: int = settings.auth_jwt.access_token_expire_minutes,
    algorithm: str = settings.auth_jwt.algorithm,
):
    now = datetime.utcnow()
    expire = now + timedelta(minutes=expire_minutes)
    to_encode = payload.copy()
    to_encode.update(
        exp=expire,
        iat=now,
    )
    encoded = jwt.encode(
        to_encode,
        private_key,
        algorithm,
    )

    return encoded


def decode_jwt(
    token: str | bytes,
    public_key: str = settings.auth_jwt.public_key_path.read_text(),
    algorithm: str = settings.auth_jwt.algorithm,
):
    decoded = jwt.decode(
        token,
        public_key,
        algorithms=[algorithm],
    )

    return decoded
