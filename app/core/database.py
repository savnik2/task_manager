from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from typing import Annotated
from fastapi import Depends

from app.core.config import DBNAME, DBPORT, DBUSER, DBPASSWORD, DBHOST


SQLALCHEMY_DATABASE_URL = (
    f"postgresql+asyncpg://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"
)


SYNC_SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DBUSER}:{DBPASSWORD}@{DBHOST}:{DBPORT}/{DBNAME}"
)



engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine,
)

sync_engine = create_engine(SYNC_SQLALCHEMY_DATABASE_URL, echo=True)

SyncSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=sync_engine,
)



async def get_db() -> AsyncSession:
    async with SessionLocal() as session:
        yield session

DBSession = Annotated[AsyncSession, Depends(get_db)]