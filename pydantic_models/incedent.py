import datetime

from pydantic import BaseModel


class Incident(BaseModel):
    id: str
    description: str
    status: str
    source: str
    created_at: datetime.date
