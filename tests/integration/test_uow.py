import pytest

from src.application import dto
from src.infrastructure.db.repositories.user import UsernameAlreadyExistError
from src.infrastructure.db.unit_of_work import SqlAlchemyUnitOfWork

USER = dto.User(
    id=1,
    username='test',
    first_name='test',
    last_name='test',
    middle_name=None,
)


async def test_add_user(sqla_uow: SqlAlchemyUnitOfWork) -> None:
    async with sqla_uow:
        await sqla_uow.user.add(USER)


async def test_uniq(sqla_uow: SqlAlchemyUnitOfWork) -> None:
    async with sqla_uow:
        await sqla_uow.user.add(USER)
    with pytest.raises(UsernameAlreadyExistError):
        async with sqla_uow:
            await sqla_uow.user.add(USER)
