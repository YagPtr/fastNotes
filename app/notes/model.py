from sqlalchemy import DateTime
from sqlalchemy import String
from app.database import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class NoteClass(Base):
    __tablename__ = "note_database"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    data: Mapped[DateTime] = mapped_column(DateTime)

    # fullname: Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, data={self.data!r})"
