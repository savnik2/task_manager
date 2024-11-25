from fastapi import Depends, HTTPException
import app.core.security as auth_security

from app.repository.user_repository import UserRepository
from app.schemas.users import UserCreate, TokenInfo


class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo: UserRepository = user_repo

    async def sign_up(
            self,
            user_data: UserCreate,
    ):
        exists_user = await self.user_repo.get(email=user_data.email)
        if exists_user:
            raise HTTPException(
                status_code=400,
                detail=f"User with email {user_data.email} already exists",
            )
        user_data.password = auth_security.create_db_password(user_data.password)
        user_dict = user_data.model_dump()
        user = await self.user_repo.create(user_dict)
        access_token = auth_security.encode_jwt(
            {'sub': str(user.id), 'email': user.email}
        )

        return TokenInfo(
            access_token=access_token
        )

    async def authentification(
            self,
            user_data
    ):
        user = await self.user_repo.get(email=user_data.username)

        if user is None:
            raise HTTPException(
                status_code=400,
                detail="You are not registered",
            )

        if not auth_security.validate_password(
                password=user_data.password, hashed_password=user.password
        ):
            raise HTTPException(
                status_code=400,
                detail="Wrong email or password",
            )

        access_token = auth_security.encode_jwt({"sub": str(user.id), "email": user.email})
        return TokenInfo(
            access_token=access_token
        )

    async def current_user(
            self, user_id,
    ):
        user = await self.user_repo.get(id=user_id)
        if user is None:
            raise HTTPException(status_code=400, detail="Пользователь не найден")
        return user
