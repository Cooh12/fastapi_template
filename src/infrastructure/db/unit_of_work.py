from __future__ import annotations

from sqlalchemy.ext.asyncio import AsyncSession

from src.application.interfaces.uow import UnitOfWork
from src.infrastructure.db.repositories.user import UserRepository


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __aenter__(self):
        self.user = UserRepository(self.session)
        return await super().__aenter__()

    async def __aexit__(self, *args):
        await super().__aexit__(*args)
        await self.session.close()

    async def commit(self) -> None:
        await self.session.commit()

    async def rollback(self) -> None:
        await self.session.rollback()
