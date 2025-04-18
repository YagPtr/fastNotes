from pydantic import BaseModel, ConfigDict


class Note(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    Note: str
    user_id:str


class NoteForSomeone(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    Note: str
    user_id:str
    executor_id:str



class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    user_id: str
    first_name: str
    last_name:str

class GetResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    visible: bool

