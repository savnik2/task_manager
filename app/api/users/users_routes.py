from typing import Annotated

from fastapi import APIRouter, Depends
from fastapi.security import (
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
)
from app.api.dependencie import (
    CurrentUser,
    oauth2_scheme,
    http_bearer, CurrentUserForRefresh,
)
from app.schemas.users import (
    UserCreate,
    UserAuth, TokenInfo, UserData,
)
from app.services.user_service import UserService

router = APIRouter(
    tags={'users'},
    dependencies=[Depends(http_bearer)]
)


@router.post(
    '/sign-up',
    summary='Регистрация',
    response_model=TokenInfo,
)
async def sign_up(
        user: UserCreate,
        user_service: UserService = Depends(),
):
    return await user_service.sign_up(user)


@router.post(
    '/sign-in',
    summary='Авторизация',
    response_model=TokenInfo,
)
async def sign_in(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        user_service: UserService = Depends()
):
    return await user_service.auth(form_data)


@router.get(
    '/users/me',
    summary='Информация профиля',
    response_model=UserData,
)
async def current_user(user: CurrentUser):
    return user

@router.post(
    '/refresh',
    summary='Выпуск нового токена',
    response_model=TokenInfo,
    response_model_exclude_none=True,
)
async def refresh_jwt(
        user: CurrentUserForRefresh,
        user_service: UserService = Depends(),
):
    return await user_service.refresh_user(user)