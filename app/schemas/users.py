from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    UUID4,
    field_validator,
    validator,
)
from pydantic.types import constr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    email: str
    name: str
    surname: str
    password: constr(strip_whitespace=True, min_length=8)


class UserAuth(BaseModel):
    username: str
    password: constr(strip_whitespace=True, min_length=8)


class UserData(BaseModel):
    id: int
    email: str
    name: str
    surname: str
    password: str


class TokenInfo(BaseModel):
    access_token: str
    # refresh_token: str
    type: str = "Bearer"
