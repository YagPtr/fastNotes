from sqlalchemy import select, delete
from app.notes.model import NoteClass
from app.database import async_session_maker
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update as sqlalchemy_update, or_

class NoteDAO:
    @classmethod
    async def find_all_students(cls):
        async with async_session_maker() as session:
            # if somedata.visible:
            #     print("visible")
            query = select(NoteClass).where(
                or_(NoteClass.visible == True, NoteClass.visible == None)
            )
            students = await session.execute(query)
            return students.scalars().all()

    @classmethod
    async def add_note(cls, note):
        async with async_session_maker() as session:
            async with session.begin():
                session.add(
                    NoteClass(
                        data=datetime.strptime(
                            datetime.now().strftime("%m-%d-%y %H:%M"), "%m-%d-%y %H:%M"
                        ),
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
    async def delete_note(cls, number):
        async with async_session_maker() as session:
            async with session.begin():
                query = (
                    sqlalchemy_update(NoteClass)
                    .where(NoteClass.id == number)
                    .values(
                        {
                            "visible": False,
                            "data_of_close": datetime.strptime(
                                datetime.now().strftime("%m-%d-%y %H:%M"),
                                "%m-%d-%y %H:%M",
                            ),
                        },
                    )
                    .execution_options(synchronize_session="fetch")
                )
                result = await session.execute(query)
                try:
                    await session.commit()
                except SQLAlchemyError as e:
                    await session.rollback()
                    raise e
                return result.rowcount
