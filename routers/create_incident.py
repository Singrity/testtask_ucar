import logging
import uuid
import datetime

from fastapi import APIRouter, Request, HTTPException, status

from pydantic_models.create_incident import CreateIncident
from pydantic_models.incedent import IncidentModel
from db_models.incident_table import Incident
from databasemanager import DATABASE_MANAGER

logger = logging.getLogger(__name__)


router = APIRouter()


@router.post("/create_incident",
             response_model=IncidentModel,
             status_code=status.HTTP_201_CREATED,
             summary="Creates an incident",
             description="Create a new incident!"
                         "status - only allow: 'normal', 'asap', 'blocking',"
                         "source - only allow: 'operator', 'monitoring', 'partner'")
async def create_incident(incident: CreateIncident) -> IncidentModel:
    new_incident = IncidentModel(
        id=str(uuid.uuid4()),
        description=incident.description,
        status=incident.status,
        source=incident.source,
        created_at=datetime.datetime.now()
    )

    async with DATABASE_MANAGER.get_session() as session:
        async with session.begin():
            try:
                created = await Incident.insert(incident=new_incident, session=session)
                if not created:
                    logger.error(f"Failed to create incident")
                    raise HTTPException(
                        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                        detail="Incident was not created!"
                    )
                return new_incident
            except Exception as e:
                logger.error(f"Failed to create incident: {e}")
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail="Failed to create incident"
                )



