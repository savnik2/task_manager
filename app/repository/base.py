from abc import ABC, abstractmethod
from sqlalchemy import select, update

from app.core.database import DBSession


class BaseRepository(ABC):
    @abstractmethod
    async def create(self, query: dict):
        raise NotImplementedError

    @abstractmethod
    async def delete(self, query: dict):
        raise NotImplementedError

    @abstractmethod
    async def get(self, *args, **kwargs):
        raise NotImplementedError


    @abstractmethod
    async def list(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def updating(self, *args, **kwargs):
        raise NotImplementedError


class SQLAlchemyRepository(BaseRepository):
    model = None

    def __init__(self, db: DBSession):
        self.db = db

    async def create(
            self,
            values: dict,
                     ):
        query = self.model(**values)
        self.db.add(query)
        await self.db.commit()
        await self.db.refresh(query)
        return query

    async def delete(
            self,
            values: dict,
                     ):
        await self.db.delete(self.model(**values))
        await self.db.commit()

    async def get(
            self,
            **data,
                  ):
        query = select(self.model).where(
            *[getattr(self.model, key) == value for key, value in data.items()])
        result = await self.db.execute(query)

        return result.scalars().first()

    async def list(
            self,
            data: dict,

    ):
        query = select(self.model).where(
            *[getattr(self.model, key) == value for key, value in data.items()])
        result = await self.db.execute(query)

        return result.scalars().all()

    async def updating(
            self,
            user_id: int,
            values: dict,
                    ):
        query = update(self.model).where(self.model.id == user_id).values(**values)
        await self.db.execute(query)
        await self.db.commit()
        return query
