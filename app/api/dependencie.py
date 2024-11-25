from fastapi import Depends, HTTPException, status
from typing import Annotated

from jwt import InvalidTokenError

import app.core.security as auth_security
from jose import JWTError
from fastapi.security import HTTPBearer, OAuth2PasswordBearer

from app.schemas.users import UserData
from app.services.user_service import UserService

# http_bearer = HTTPBearer()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/sign-in')


def credentials_exception(
        details="Unauthorization",
):
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=details,
        headers={"WWW-Authenticate": "Bearer"},
    )


async def validate_token(access_token: str = Depends(oauth2_scheme)):
    try:
        # if credentials is None:
        #     raise credentials_exception(
        #         details="Token is not definded"
        #     )
        # access_token = credentials.credentials
        payload = auth_security.decode_jwt(access_token)
        if payload is None:
            raise credentials_exception()

        user_id = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception()

        return user_id
    except InvalidTokenError:
        raise credentials_exception(
            details="Token is invalid"
        )


async def get_user_by_id(user_id: int, user_service: UserService = Depends()):
    user = await user_service.current_user(user_id)
    if user is None:
        raise credentials_exception()
    return user


async def get_current_user(user_id: int = Depends(validate_token), user_service: UserService = Depends()):
    return await get_user_by_id(user_id, user_service)


CurrentUser = Annotated[UserData, Depends(get_current_user)]
