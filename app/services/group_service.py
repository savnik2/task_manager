from fastapi import Depends

from app.repository.group_repository import GroupRepository
from app.schemas.groups import CreateGroup

class GroupService:
    def __init__(
            self, group_repo: GroupRepository = Depends(),
    ):
        self.group_repo: GroupRepository = group_repo

    async def create_group(
            self,
            user_id: int,
            group_data: CreateGroup,
    ):

        return await self.group_repo.create(group_data.model_dump())


