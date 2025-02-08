from sqlalchemy import DateTime
from sqlalchemy import String, Boolean
from app.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional


class NoteClass(Base):
    __tablename__ = "note_database"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    data: Mapped[DateTime] = mapped_column(DateTime)
    author: Mapped[Optional[str]] = mapped_column(String(100))
    executor: Mapped[Optional[str]] = mapped_column(String(100))
    visible: Mapped[Optional[bool]] = mapped_column(Boolean, default=True)
    data_of_close: Mapped[Optional[DateTime]] = mapped_column(DateTime)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, data={self.data!r}, data_of_close={self.data_of_close!r})"
