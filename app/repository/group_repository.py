from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.models import Groups, user_group_association
from app.repository.base import SQLAlchemyRepository



class GroupRepository(SQLAlchemyRepository):
    model = Groups

    async def get_group_with_members(
            self,
            group_id: int,
    ):
        query = select(self.model).where(
            self.model.id == group_id).options(selectinload(self.model.members))
        result = await self.db.execute(query)

        return result.scalars().first()
    async def add_member(
            self,
            user_id: int,
            group_id: int,
    ):
        query = user_group_association.insert().values(
            user_id = user_id,
            group_id = group_id,
        )
        await self.db.execute(query)
        await self.db.commit()


