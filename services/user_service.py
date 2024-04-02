from fastapi import Depends, HTTPException
import utils.security as auth_security

from models.users import Users
from repository.user_repository import UserRepository
from schemas.users import UserCreate


class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo: UserRepository = user_repo

    async def sign_up(self, user_data: UserCreate):
        exists_user = await self.user_repo.get({"email": user_data.email})
        if exists_user:
            raise HTTPException(
                status_code=400,
                detail=f"User with email {user_data.email} already exists",
            )
        user_data.password = auth_security.create_db_password(user_data.password)
        user_dict = user_data.model_dump()
        user = await self.user_repo.create(user_dict)
        access_token = auth_security.create_jwt_token(
            {'sub': str(user.id),  'email': user.email})
        return {'access_token': access_token,"token_type": "Bearer"}