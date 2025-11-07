from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert

from settings import AppSettings

class CRUD:

    @classmethod
    async def upsert(
            cls,
            data: list[dict],
            validation_model: type,
            session: AsyncSession,
            conflict_constraint: str = None,
            chunk_size: int = AppSettings.CHUNK_SIZE,
            ):
        pass

        for i in range(0, len(data), chunk_size):
            chunk = data[i: i + chunk_size]
            validated_data = [validation_model(**chunk_item).model_dump() for chunk_item in chunk]

            stmt = (insert(cls).values(validated_data))