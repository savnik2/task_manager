import hashlib, string, random
from datetime import datetime, timedelta
import jwt

from app.core.config import settings
from app.schemas.users import UserData


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


def create_db_password(
        password
):
    salt = get_random_string()
    hashed_password = hash_password(password, salt)
    new_password = f"{salt}${hashed_password}"
    return new_password


def validate_password(
        password: str,
        hashed_password: str
):
    salt, hashed = hashed_password.split("$")
    return hash_password(password, salt) == hashed


def encode_jwt(
        payload: dict,
        expire_minutes: int,
        private_key: str = settings.auth_jwt.private_key_path.read_text(),
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


def create_access(
        user: UserData,
):
    payload = {
        'sub': user.id,
        'email': user.email,
        'type': 'access'
    }
    return encode_jwt(
        payload,
        expire_minutes=settings.auth_jwt.access_token_expire_minutes,
    )


def create_refresh(
        user: UserData,
):
    payload = {
        'sub': user.id,
        'type': 'refresh'
    }
    return encode_jwt(
        payload,
        expire_minutes=settings.auth_jwt.refresh_token_expire_minutes,
    )
