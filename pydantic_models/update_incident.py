import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic_models.enums import Status, Source


class UpdateIncidentModel(BaseModel):
    """
    Model for validation when updating incident
    """

    description: Optional[str] = None
    status: Optional[Status] = None
    source: Optional[Source] = None

    model_config = ConfigDict(
        use_enum_values=True,
    )
