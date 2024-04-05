from fastapi import APIRouter, Depends

from app.api.dependencie import CurrentUser
from app.schemas.users import UserCreate
from app.services.user_service import UserService

router = APIRouter(tags={'users'})


@router.post('/sign-up')
async def sign_up(user: UserCreate, usr_service: UserService = Depends()):
    return await usr_service.sign_up(user)


@router.post('/sign-in')
async def sign_in(user: UserCreate, usr_service: UserService = Depends()):
    return await usr_service.authentification(user)

@router.get('/users/me')
async def current_user(user: CurrentUser):
    return user