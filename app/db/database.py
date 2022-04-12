from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from os import getenv

POSTGRES_CREDENTIALS = {
    "username": "postgres",
    "password": "qwerty",
    "drivername": "postgresql+asyncpg",
    "database": "postgres",
    "host": "db",
    "port": "5432"
}

engine = create_async_engine(URL(**POSTGRES_CREDENTIALS))
maker = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    expire_on_commit=False,
    class_= AsyncSession
)

Base = declarative_base()

class DbSession:
    def __init__(self) -> None:
        self.__session_instance: AsyncSession = None

    async def __aenter__(self) -> AsyncSession:
        self.__session_instance = maker()
        return self.__session_instance

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.__session_instance.close()