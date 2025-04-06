from fastapi import APIRouter
from app.notes.dao import NoteDAO
from app.notes.note import Note,User,NoteForSomeone
from typing import Optional
router = APIRouter(prefix="/notes", tags=["Работа с записями"])


@router.get("/", summary="Получить все записи")
async def get_all_notes():
    return await NoteDAO.find_all_students()

@router.post("/exec/", summary="Добавление записи для кого-то")
async def add_note(note: NoteForSomeone):
    check = await NoteDAO.add_note_for_someone(note)
    return check


@router.post("/", summary="Добавление записи")
async def add_note(note: Note):
    check = await NoteDAO.add_note(note)
    return check


@router.get("/{amount}", summary="Получить записи по идентификатору владельца")
async def get_note_with_number(amount: str = None):
    return await NoteDAO.find_notes(amount)


@router.get("/exec/{amount}", summary="Получить назначенные записи по идентификатору владельца")
async def get_note_with_number_as_executor(amount: str = None):
    return await NoteDAO.find_notes_as_executor(amount)


@router.get("/completed/{amount}", summary="Завершенные задачи")
async def get_closes_note_with_number(amount: str = None):
    return await NoteDAO.find_notes_completed(amount)



@router.delete("/{amount}", summary="Удалить запись")
async def delete_note_with_number(amount: Optional[int] = None):
    return await NoteDAO.delete_note(amount)

@router.post("/register/", summary="Добавить пользователя")
async def register_user(user:User):
    return await NoteDAO.add_user(user)

@router.get("/user/{amount}", summary="Получить идентификатор пользователя")
async def get_user_id(amount:str):
    return await NoteDAO.find_user_by_name(amount)

@router.get("/data/{amount}", summary="Получить запись по идентификатору")
async def get_note_by_id(amount:int):
    return await NoteDAO.get_note_with_its_id(amount)