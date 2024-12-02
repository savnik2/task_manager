from fastapi import (
    Depends,
    HTTPException,
    status,
)

from typing import Annotated

from jwt import InvalidTokenError

import app.core.security as auth_security
from fastapi.security import (
    HTTPBearer,
    OAuth2PasswordBearer
)

from app.schemas.users import UserData
from app.services.user_service import UserService

http_bearer = HTTPBearer(auto_error=False)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/sign-in')


def credentials_exception(
        details: str = "Unauthorization",
):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=details,
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_jwt_payload(
        token: str = Depends(oauth2_scheme),
):
    try:
        payload = auth_security.decode_jwt(token)
        if payload is None:
            raise credentials_exception()
        return payload
    except InvalidTokenError:
        raise credentials_exception(
            details="Token is invalid"
        )


async def validate_token(
        payload: dict,
        token_type: str,
):

    current_type = payload.get("type")
    if current_type == token_type:
        return
    raise credentials_exception(
        details=f'Invalid token type: expected {token_type!r}, current: {current_type!r}'
    )


async def get_current_user(
        payload: dict = Depends(get_jwt_payload),
        user_service: UserService = Depends(),

):
    await validate_token(payload, 'access')
    user_id = int(payload.get("sub"))
    if user_id is None:
        raise credentials_exception()

    user = await user_service.current_user(user_id)
    if user is None:
        raise credentials_exception()
    return user


async def get_current_user_for_refresh(
        payload: dict = Depends(get_jwt_payload),
        user_service: UserService = Depends(),

):
    await validate_token(payload, 'refresh')
    user_id = int(payload.get("sub"))
    if user_id is None:
        raise credentials_exception()

    user = await user_service.current_user(user_id)
    if user is None:
        raise credentials_exception()
    return user


CurrentUser = Annotated[UserData, Depends(get_current_user)]
CurrentUserForRefresh = Annotated[UserData, Depends(get_current_user_for_refresh)]
