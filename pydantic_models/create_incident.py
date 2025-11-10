from pydantic import BaseModel
from pydantic_models.enums import Source, Status


class CreateIncident(BaseModel):
    """
    Model for validation when creating incident
    """
    description: str
    status: Status
    source: Source
