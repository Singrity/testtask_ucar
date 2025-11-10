from fastapi import APIRouter, status
from pydantic_models.incedent import IncidentModel
from pydantic_models.enums.statuses import Status
from db_models.incident_table import Incident
from databasemanager import DATABASE_MANAGER
router = APIRouter()


@router.get("/get_incidents_by_status",
            response_model=list[IncidentModel],
            status_code=status.HTTP_200_OK,
            summary="Get a list of incidents by status filter",
            description="Returns list of all incidents filtered by status")
async def get_incidents_by_status(status: Status):
    async with DATABASE_MANAGER.get_session() as session:
        async with session.begin():
            incidents_list = await Incident.get_by_status(status.value, session)
            return incidents_list


