import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic_models.enums import Source, Status


class IncidentModel(BaseModel):
    """
    Model for full database table validation
    """
    id: str
    description: str
    status: Status
    source: Source
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime] = None

    model_config = ConfigDict(
        use_enum_values=True,
    )







