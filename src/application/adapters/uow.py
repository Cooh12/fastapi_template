from typing import Protocol

from src.application.adapters.user import UserAdapters


class UnitOfWork(Protocol):
    user: UserAdapters

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.rollback()

    async def commit(self) -> None:
        raise NotImplementedError

    async def rollback(self) -> None:
        raise NotImplementedError
