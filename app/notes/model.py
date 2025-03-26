from sqlalchemy import DateTime
from sqlalchemy import String, Boolean
from app.database import Base, str_uniq, int_pk, str_null_true
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import Optional
from sqlalchemy import ForeignKey, text, Text
from datetime import date
class NoteClass(Base):
    __tablename__ = "note_database"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    data: Mapped[DateTime] = mapped_column(DateTime)
    # author: Mapped[Optional[str]] = mapped_column(String(100))
    executor: Mapped[Optional[str]] = mapped_column(String(100))
    visible: Mapped[Optional[bool]] = mapped_column(Boolean, default=True)
    data_of_close: Mapped[Optional[DateTime]] = mapped_column(DateTime)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), nullable=False)
    user: Mapped["User"] = relationship("User")


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, data={self.data!r}, data_of_close={self.data_of_close!r})"




# создаем модель таблицы студентов
class   User(Base):
    __tablename__ = "User"
    id: Mapped[int_pk]
    # phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    # date_of_birth: Mapped[date]
    # email: Mapped[str_uniq]
    # address: Mapped[str] = mapped_column(Text, nullable=False)
    # enrollment_year: Mapped[int]
    # course: Mapped[int]
    # special_notes: Mapped[str_null_true]
    # major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)
    #
    # major: Mapped["Major"] = relationship("Major", back_populates="students")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)


# создаем модель таблицы факультетов (majors)
# class Major(Base):
#     id: Mapped[int_pk]
#     major_name: Mapped[str_uniq]
#     major_description: Mapped[str_null_true]
#     count_students: Mapped[int] = mapped_column(server_default=text('0'))
#
#     def __str__(self):
#         return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"
#
#     def __repr__(self):
#         return str(self)



# class Student2(Base):
#     id: Mapped[int_pk]
#     phone_number: Mapped[str_uniq]
#     first_name: Mapped[str]
#     last_name: Mapped[str]
#     date_of_birth: Mapped[date]
#     email: Mapped[str_uniq]
#     address: Mapped[str] = mapped_column(Text, nullable=False)
#     enrollment_year: Mapped[int]
#     course: Mapped[int]
#     special_notes: Mapped[str_null_true]
#     major_id: Mapped[int] = mapped_column(ForeignKey("majors.id"), nullable=False)
#
#     major: Mapped["Major"] = relationship("Major", back_populates="students")
#
#     def __str__(self):
#         return (f"{self.__class__.__name__}(id={self.id}, "
#                 f"first_name={self.first_name!r},"
#                 f"last_name={self.last_name!r})")
#
#     def __repr__(self):
#         return str(self)

