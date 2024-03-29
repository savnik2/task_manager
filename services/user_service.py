from fastapi import Depends

from models.users import Users
from repository.user_repository import UserRepository
from schemas.users import UserData


class UserService:
    def __init__(self, user_repo: UserRepository = Depends()):
        self.user_repo: UserRepository = user_repo

    async def sign_up(self, user_data: UserData):
        user_dict = user_data.model_dump()
        user = await self.user_repo.create(user_dict)
        return user