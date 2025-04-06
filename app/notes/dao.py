from fontTools.merge.util import first
from sqlalchemy import select, delete
from app.notes.model import NoteClass,User
from app.database import async_session_maker
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import update as sqlalchemy_update, or_
from app.utils import logEvent
from datetime import datetime

class NoteDAO:
    @classmethod
    async def find_all_students(cls):
        async with async_session_maker() as session:
            logEvent(str(datetime.now()))
            query = select(NoteClass).where(
                or_(NoteClass.visible == True, NoteClass.visible == None)
            )
            students = await session.execute(query)
            logEvent("Успешный запрос всех записей")
            return students.scalars().all()

    @classmethod
    async def add_note(cls, note):
        async with async_session_maker() as session:
            async with session.begin():
                logEvent(str(datetime.now()))
                session.add(
                    NoteClass(
                        data=datetime.strptime(
                            datetime.now().strftime("%m-%d-%y %H:%M"), "%m-%d-%y %H:%M"
                        ),
                        name=note.Note,
                        user_id=note.user_id
                    )
                )
                try:
                    await session.commit()
                    logEvent("Успешное добавление записи")
                except SQLAlchemyError as e:
                    await session.rollback()
                    logEvent(e)
                    return "note was not added"
                return "note was added"


    @classmethod
    async def add_user(cls, user):
        async with async_session_maker() as session:
            async with session.begin():
                logEvent(str(datetime.now()))
                session.add(
                    User(
                        id=user.user_id,
                        first_name=user.first_name,
                        last_name=user.last_name

                    )
                )
                try:
                    await session.commit()
                    logEvent("Успешное добавление пользователя "+ user.user_id)
                except SQLAlchemyError as e:
                    await session.rollback()
                    logEvent(e)
                    return "user was not added"
                return "user was added"
            

    @classmethod
    async def find_notes(cls, number: int):
        async with async_session_maker() as session:
            logEvent(str(datetime.now()))
            query = select(NoteClass).where(NoteClass.user_id == number).where(or_(NoteClass.visible == True))
            students = await session.execute(query)
            return students.scalars().first()
        
    @classmethod
    async def find_notes_as_executor(cls, number: int):
        async with async_session_maker() as session:
            logEvent(str(datetime.now()))
            query = select(NoteClass).where(NoteClass.executor == number).where(or_(NoteClass.visible == True))
            students = await session.execute(query)
            return students.scalars().all()
        
    @classmethod
    async def find_user_by_name(cls, number: str):
        async with async_session_maker() as session:
            logEvent(str(datetime.now()))
            query = select(User).where(User.first_name == number)
            students = await session.execute(query)
            return students.scalars().all()
        
    @classmethod
    async def find_notes_completed(cls, number: int):
        async with async_session_maker() as session:
            logEvent(str(datetime.now()))
            query = select(NoteClass).where(NoteClass.user_id == number).where(or_(NoteClass.visible == False,NoteClass.visible==None))
            students = await session.execute(query)
            return students.scalars().all()


    @classmethod
    async def delete_note(cls, number):
        async with async_session_maker() as session:
            async with session.begin():
                logEvent(str(datetime.now()))
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
                    logEvent("Успешное удаление заметки "+str(number))
                except SQLAlchemyError as e:
                    await session.rollback()
                    # raise e
                return result.rowcount

    @classmethod
    async def add_note_for_someone(cls, note):

        async with async_session_maker() as session:
            async with session.begin():
                logEvent(str(datetime.now()))
                session.add(
                    NoteClass(
                        data=datetime.strptime(
                            datetime.now().strftime("%m-%d-%y %H:%M"), "%m-%d-%y %H:%M"
                        ),
                        name=note.Note,
                        user_id=note.user_id,
                        executor=note.executor_id
                    )
                )
                try:
                    await session.commit()
                    logEvent("Успешное добавление записи")
                except SQLAlchemyError as e:
                    await session.rollback()
                    logEvent(e)
                    return "note was not added"
                return "note was added"
            
    @classmethod
    async def get_note_with_its_id(cls,number):
        async with async_session_maker() as session:
            logEvent(str(datetime.now()))
            query = select(NoteClass).where(
                NoteClass.id==number
            )
            students = await session.execute(query)
            logEvent("Успешный запрос записи по номеру")
            return students.scalars().all()