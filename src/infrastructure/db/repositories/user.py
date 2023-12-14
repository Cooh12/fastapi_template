from sqlalchemy import select

from src.application import dto
from src.application.interfaces.user import UserAdapters
from src.infrastructure.db.models import User
from src.infrastructure.db.repositories.base import SqlAlchemyRepository


class UsernameAlreadyExistError(Exception):
    username: str

    @property
    def message(self) -> str:
        return f'A username "{self.username}" already exists'


class UserRepository(SqlAlchemyRepository, UserAdapters):
    async def add(self, user: dto.User) -> None:
        user = User(
            username=user.username,
            first_name=user.first_name,
            last_name=user.last_name,
            middle_name=user.middle_name
        )
        self._session.add(user)

    async def get_by_id(self, user_id: dto.UserId) -> dto.User:
        user = await self._session.scalar(select(User).where(User.id == user_id))
        if not user:
            raise Exception  # TODO: доделать ошибки

        return user.to_dto()

    def _parse_error(self, user: dto.User) -> None:  # noqa # type: ignore
        match err.__cause__.__cause__.constraint_name:  # type: ignore
            case 'uq__users__username':
                raise UsernameAlreadyExistError(username=user.username)
            case _:
                raise Exception
