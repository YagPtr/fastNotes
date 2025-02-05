from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from app.config import DBpath
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from datetime import datetime
from sqlalchemy import DateTime


class Base(DeclarativeBase):
    pass


class NoteClass(Base):
    __tablename__ = "note_database"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    data: Mapped[DateTime] = mapped_column(DateTime)
    data2: Mapped[str] = mapped_column(String(100), nullable=True)
    data3: Mapped[str] = mapped_column(String(100), nullable=True)

    # fullname: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, data={self.data!r})"


# with Session(engine) as session:
#     session.add(Note(id=1, name="ssdss"))

#     session.commit()
# stmt = select(Note)


# for user in session.scalars(stmt):
#     print(user)
def create():
    engine = create_engine(DBpath, echo=True)

    Base.metadata.create_all(engine)
    with Session(engine) as session:
        session.add(NoteClass(id=2, name="ssdss", data=datetime.now()))

        session.commit()
