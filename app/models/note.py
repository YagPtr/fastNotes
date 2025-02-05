from pydantic import BaseModel, ConfigDict
from datetime import datetime


class Note(BaseModel):
    data: str
    Note: str

    class Config:
        validate_assignment = True
