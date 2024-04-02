from typing import Annotated
from fastapi import APIRouter, Depends

from schemas.users import UserCreate
from services.user_service import UserService

router = APIRouter(tags={'users'})


@router.post('/sign-up')
async def sign_up(user: UserCreate, usr_service: UserService = Depends()):
    return await usr_service.sign_up(user)
