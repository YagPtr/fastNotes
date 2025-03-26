from pydantic import BaseModel, ConfigDict


class Note(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    Note: str
    user_id:int


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: int
    first_name: str
    last_name:str

class GetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    visible: bool

