from fastapi import Depends, HTTPException, status, Header

from typing import Annotated
import utils.security as auth_security
from jose import JWTError

async def get_current_user(access_token: str =  Header(default=None), user_service: UserService = Depends()):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Вы не авторизованы",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        if access_token is None:
            raise credentials_exception
        payload = auth_security.verify_jwt_token(access_token)
        if payload is None:
            raise credentials_exception
        user_id = int(payload.get("sub"))
        if user_id is None:
            raise credentials_exception
        user = await user_service.current_user(user_id)
        if user is None:
            raise credentials_exception
        return user
    except JWTError:
        raise credentials_exception


CurrentUser = Annotated[Depends(get_current_user)]