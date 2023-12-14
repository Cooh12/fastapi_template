from src.application import dto
from src.application.interfaces.uow import UnitOfWork


async def add_user(user: dto.User, uow: UnitOfWork) -> None:
    async with uow:
        await uow.user.add(user)


async def get_user_by_id(user_id: dto.UserId, uow: UnitOfWork) -> dto.User:
    async with uow:
        return await uow.user.get_by_id(user_id)
