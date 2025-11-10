import logging

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager

from settings import DBSettings
from db_models.base_table import Base

logger = logging.getLogger(__name__)


class DatabaseManager:

    def __init__(self, schema: str = 'public'):
        self.schema = schema

        self.username = DBSettings.DB_USERNAME
        self.password = DBSettings.DB_PASSWORD
        self.host = DBSettings.DB_HOST
        self.port = DBSettings.DB_PORT
        self.name = DBSettings.DB_NAME

        self.uri = f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.name}"

        self.engine = create_async_engine(self.uri, echo=False, future=True, pool_recycle=1800, pool_pre_ping=True)

        self._session_factory = sessionmaker(self.engine, class_=AsyncSession, expire_on_commit=False)

    async def create_tables(self):
        try:
            async with self.engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all, checkfirst=True)
                logger.info(f"Tables created successfully in schema '{self.schema}'")
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            raise

    @asynccontextmanager
    async def get_session(self):
        async_session = self._session_factory()
        try:
            yield async_session
        except Exception as e:
            await async_session.rollback()
            raise e
        finally:
            await async_session.close()


DATABASE_MANAGER = DatabaseManager()
