from src.application.interfaces.uow import UnitOfWork
from tests.mocks.repository import UserFakeRepository


class FakeUnitOfWork(UnitOfWork):
    committed = False
    user = UserFakeRepository()

    async def commit(self) -> None:
        self.committed = True

    async def rollback(self) -> None:
        pass
