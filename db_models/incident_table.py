import logging

import sqlalchemy.ext.asyncio
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import Column, String, DateTime
from sqlalchemy import insert, update, select
from db_models.base_table import Base
from pydantic_models.incedent import IncidentModel

logger = logging.getLogger(__name__)


class Incident(Base):
    __tablename__ = "incidents"
    __table_args__ = {"schema": "public"}

    id = Column(String, primary_key=True)
    description = Column(String)
    status = Column(String)
    source = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, nullable=True)

    @classmethod
    async def insert(cls, incident: IncidentModel, session: sqlalchemy.ext.asyncio.AsyncSession) -> bool:

        stmt = insert(cls).values(incident.model_dump())
        try:
            await session.execute(stmt)
            logger.info(f"Insert into {cls.__tablename__}")
            return True
        except SQLAlchemyError as e:
            logger.error(f"{cls.__tablename__} insertion error: {e}")
            return False

    @classmethod
    async def update(
            cls,
            incident_id: str,
            data: dict,
            session: sqlalchemy.ext.asyncio.AsyncSession) -> 'Incident | None':
        stmt = update(cls).where(cls.id == incident_id).values(data).returning(cls)
        try:
            result = await session.execute(stmt)
            incident = result.scalar_one_or_none()

            if incident is None:
                logger.warning(f"Incident not found for update: {incident_id}")
                return None

            logger.info(f"Update {cls.__tablename__}")
            return incident
        except SQLAlchemyError as e:
            logger.error(f"{cls.__tablename__} update error: {e}")
            return None

    @classmethod
    async def get_by_status(cls, status: str, session: sqlalchemy.ext.asyncio.AsyncSession) -> list:
        stmt = select(cls).where(cls.status == status)
        try:
            result = await session.execute(stmt)
            incidents = result.scalars().all()
            return incidents
        except SQLAlchemyError as e:
            logger.error(f"Something went wrong while getting {cls.__tablename__} by status: {status} - {e}")
            return []

