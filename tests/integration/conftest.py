import pytest_asyncio
from sqlalchemy.ext.asyncio import AsyncSession

from src.infrastructure.db.unit_of_work import SqlAlchemyUnitOfWork


@pytest_asyncio.fixture
async def sqla_uow(session: AsyncSession) -> SqlAlchemyUnitOfWork:
    return SqlAlchemyUnitOfWork(session)
