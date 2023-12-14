from src.api.service_layer import add_user, get_user_by_id
from src.application import dto
from tests.mocks.uow import FakeUnitOfWork

USER = dto.User(
    id=1,
    username='test',
    first_name='test',
    last_name='test',
    middle_name=None,
)


async def test_add_user(fake_uow: FakeUnitOfWork) -> None:
    await add_user(USER, fake_uow)
    return fake_uow.committed


async def test_get_user_by_id(fake_uow: FakeUnitOfWork) -> None:
    await add_user(USER, fake_uow)
    return await get_user_by_id(USER.id, fake_uow)
