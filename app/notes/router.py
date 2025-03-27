from fastapi import APIRouter
from app.notes.dao import NoteDAO
from app.notes.note import Note,User
from typing import Optional
router = APIRouter(prefix="/notes", tags=["Работа с записями"])


@router.get("/", summary="Получить все записи")
async def get_all_notes():
    return await NoteDAO.find_all_students()


@router.post("/", summary="Добавление записи")
async def add_note(note: Note):
    check = await NoteDAO.add_note(note)
    return check


@router.get("/{amount}", summary="Получить записи по идентификатору владельца")
async def get_note_with_number(amount: str = None):
    return await NoteDAO.find_notes(amount)

@router.get("/completed/{amount}", summary="Завершенные задачи")
async def get_note_with_number(amount: str = None):
    return await NoteDAO.find_notes_completed(amount)




@router.delete("/{amount}", summary="Удалить запись")
async def delete_note_with_number(amount: Optional[int] = None):
    return await NoteDAO.delete_note(amount)

@router.post("/register/", summary="Добавить пользователя")
async def register_user(user:User):
    return await NoteDAO.add_user(user)
