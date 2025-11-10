import datetime

from fastapi import APIRouter, status, HTTPException
from db_models.incident_table import Incident
from pydantic_models.incedent import IncidentModel
from pydantic_models.update_incident import UpdateIncidentModel
from databasemanager import DATABASE_MANAGER


router = APIRouter()


@router.put("/update_incident",
            response_model=IncidentModel,
            status_code=status.HTTP_200_OK,
            summary="Update an existing incident by id",
            description="Update an existing incident by id. Returns updated incident!"
                        "status - only allow: 'normal', 'asap', 'blocking',"
                        "source - only allow: 'operator', 'monitoring', 'partner'")
async def update_incident(incident_id, update_data: UpdateIncidentModel):
    update_dict = update_data.model_dump(exclude_unset=True)
    update_dict['updated_at'] = datetime.datetime.now()

    if not update_dict:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No update data provided in the request body.",
        )

    async with DATABASE_MANAGER.get_session() as session:
        async with session.begin():
            updated_incident = await Incident.update(
                incident_id=incident_id,
                data=update_dict,
                session=session
            )
            if updated_incident is None:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Incident with id '{incident_id}' not found.",
                )

    return updated_incident
