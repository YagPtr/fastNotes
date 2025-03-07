from pydantic import BaseModel, ConfigDict


class Note(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    Note: str
    author:str


class GetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    visible: bool
