Для работы с SQLite в асинхронном режиме в Python можно использовать несколько библиотек. Вот некоторые из наиболее популярных:

aiosqlite:

Это обертка над стандартной библиотекой sqlite3, которая добавляет поддержку асинхронного программирования с использованием asyncio.
Установка: pip install aiosqlite
Пример использования:
Python
Копировать
import aiosqlite
import asyncio

async def main():
    async with aiosqlite.connect('example.db') as db:
        async with db.execute('SELECT * FROM my_table') as cursor:
            async for row in cursor:
                print(row)

asyncio.run(main())
SQLAlchemy с поддержкой асинхронности:

SQLAlchemy — это мощный ORM для Python, который также поддерживает асинхронные операции с использованием asyncio.
Установка: pip install sqlalchemy aiosqlite
Пример использования:
Python
Скопировать
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
import asyncio

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String)

async def main():
    engine = create_async_engine('sqlite+aiosqlite:///example.db', echo=True)
    async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

    async with async_session() as session:
        result = await session.execute(select(MyTable))
        for row in result.scalars():
            print(row)

asyncio.run(main())
Tortoise-ORM:

Это асинхронный ORM, который также поддерживает SQLite и другие базы данных.
Установка: pip install tortoise-orm
Пример использования:
Python
Копировать
from tortoise import Tortoise, fields
from tortoise.models import Model
import asyncio

class MyTable(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=50)

async def main():
    await Tortoise.init(db_url='sqlite://example.db', modules={'models': ['__main__']})
    await Tortoise.generate_schemas()
    await MyTable.create(name='example')

    all_entries = await MyTable.all()
    for entry in all_entries:
        print(entry.name)

    await Tortoise.close_connections()

asyncio.run(main())
Эти библиотеки обеспечивают удобный и эффективный способ работы с SQLite в асинхронном режиме. Выбор конкретной библиотеки зависит от Ваших потребностей: если Вам нужен простой доступ к базе данных, aiosqlite будет отличным выбором. Если Вы хотите использовать ORM, то SQLAlchemy или Tortoise-ORM подойдут лучше.