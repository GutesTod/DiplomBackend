from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy import create_engine
from .settings import settings

engine = create_engine(settings.db_url)


async def get_session():
    session = sessionmaker(engine, expire_on_commit=False)
    return session


class Base(DeclarativeBase):
    pass