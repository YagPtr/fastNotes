from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
import json
import sqlalchemy
from sqlalchemy import create_engine
from fastapi.exceptions import RequestValidationError
from fastapi.encoders import jsonable_encoder

# from fastapi
from app.utils import result_to_response
from typing import Optional
from app.config import DBpath
from app.models.note import Note
from sqlalchemy.orm import Session
from sqlalchemy import engine
from sqlalchemy import select, delete
from app.database import NoteClass
from datetime import datetime

app = FastAPI()

engine = create_engine(DBpath, echo=True)

session = Session(engine)


class RBNote:
    def __init__(self, amount: Optional[int]):
        self.amount = amount


@app.get("/notes/")
@app.get("/notes/{amount}")
def read_root(amount: Optional[str] = None):
    if amount is None:
        result = session.scalars(select(NoteClass))
    else:
        result = session.scalars(select(NoteClass).where(NoteClass.id == amount))

    return HTMLResponse(content=result_to_response(result))


@app.post("/notes/")
async def register_user(note: Note):
    try:
        note = Note(data=note.data, Note=note.Note)

    except:
        return HTMLResponse(status_code=500, content={"error": "wrong data format"})
    session.add(
        NoteClass(data=datetime.strptime(note.data, "%m-%d-%y %H:%M"), name=note.Note)
    )
    session.commit()
    return "data was add"


@app.delete("/notes/{number}")
async def delete_note(number: int):
    # session.scalars(delete(NoteClass).where(NoteClass.id == number))
    noteFroDelete = session.get(NoteClass, number)
    session.flush()
    try:
        session.delete(noteFroDelete)
    except:
        return "data was not deleted"
    session.commit()

    return "data was deleted"


@app.exception_handler(RequestValidationError)
async def cust(request: RequestValidationError, exc: RequestValidationError):
    if request.url.path == "/notes/":
        return HTMLResponse(
            status_code=502,
            content=json.dumps({"detail": exc.errors(), "body": exc.body}),
        )
    else:
        return HTMLResponse(
            status_code=422,
            content=json.dumps({"detail": exc.errors(), "body": exc.body}),
        )
