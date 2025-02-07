from sqlalchemy import select, delete
from app.notes.model import NoteClass
from app.database import async_session_maker
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError


class NoteDAO:
    @classmethod
    async def find_all_students(cls):
        async with async_session_maker() as session:
            query = select(NoteClass)
            students = await session.execute(query)
            return students.scalars().all()

    @classmethod
    async def add_note(cls, note):
        async with async_session_maker() as session:
            async with session.begin():
                session.add(
                    NoteClass(
                        data=datetime.strptime(note.data, "%m-%d-%y %H:%M"),
                        name=note.Note,
                    )
                )
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    print(e)
                    return "note was not added"
                return "note was added"

    @classmethod
    async def find_notes(cls, number: int):
        async with async_session_maker() as session:
            query = select(NoteClass).where(NoteClass.id == number)
            students = await session.execute(query)
            return students.scalars().all()

    @classmethod
    async def delete_note(cls, number: int):
        async with async_session_maker() as session:
            query = delete(NoteClass).where(NoteClass.id == number)
            await session.execute(query)
            await session.commit()
            return "whatever"
