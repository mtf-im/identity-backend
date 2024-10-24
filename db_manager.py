import logging
from collections.abc import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

engine = create_async_engine(
    "sqlite+aiosqlite:///data.db",
    future=True,
    connect_args={"check_same_thread": False},
)

session_maker = async_sessionmaker(engine)


async def get_db() -> AsyncGenerator[AsyncSession]:
    async with session_maker() as db:
        yield db
