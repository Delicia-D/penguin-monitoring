from pydantic import BaseModel
from datetime import datetime

class UploadVisit(BaseModel):
    weight: float
    timestamp: datetime
    rfid: str
