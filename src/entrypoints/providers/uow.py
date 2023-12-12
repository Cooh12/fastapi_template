from typing import AsyncIterator

from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.infrastructure.service_layer.unit_of_work import SqlAlchemyUnitOfWork


def uow_provider() -> SqlAlchemyUnitOfWork:
    raise NotImplementedError


class UnitOfWorkProvider:
    def __init__(self, pool: async_sessionmaker[AsyncSession]):
        self.pool = pool

    async def uow(self) -> AsyncIterator[SqlAlchemyUnitOfWork]:
        async with self.pool() as session:
            yield SqlAlchemyUnitOfWork(session=session)
