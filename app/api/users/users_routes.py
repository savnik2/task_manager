from typing import Annotated

from fastapi import APIRouter, Depends, Form
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from app.api.dependencie import CurrentUser, oauth2_scheme
from app.schemas.users import UserCreate, UserAuth
from app.services.user_service import UserService

router = APIRouter(tags={'users'})



@router.post('/sign-up',
             summary='Регистрация')
async def sign_up(user: UserCreate, usr_service: UserService = Depends()):
    return await usr_service.sign_up(user)


@router.post('/sign-in',
             summary='Авторизация')
async def sign_in(
        form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
        usr_service: UserService = Depends()
):
    return await usr_service.authentification(form_data)


@router.get('/users/me',
            summary='Информация профиля')
async def current_user(user: CurrentUser):
    return user
