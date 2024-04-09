from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.users import Projects
from app.repository.base import SQLAlchemyRepository


class ProjectRepository(SQLAlchemyRepository):
    model = Projects

    async def get_project_with_tasks(
            self,
            data,
    ):

        query = (select(self.model).where(
            *[getattr(self.model, key) == value for key, value in data.items()]).
                 options(selectinload(self.model.task)))
        result = await self.db.execute(query)

        return result.scalars().first()
