from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    meta_data = MetaData()

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}