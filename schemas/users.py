from pydantic import BaseModel, EmailStr, Field, UUID4, field_validator, validator
from pydantic.types import constr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):

    email: EmailStr
    password: constr(strip_whitespace=True, min_length=8)


class UserData(BaseModel):
    id: int
    email: EmailStr
    password: str




