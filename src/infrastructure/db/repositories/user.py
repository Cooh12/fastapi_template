from sqlalchemy import select

from src.application import dto
from src.application.adapters.user import UserAdapters
from src.infrastructure.db.models import User
from src.infrastructure.db.repositories.base import SqlAlchemyRepository


class UserRepository(SqlAlchemyRepository, UserAdapters):
    async def add(self, user: dto.User) -> None:
        self._session.add(user)

    async def get_by_id(self, user_id: dto.UserId) -> dto.User:
        user = await self._session.scalar(select(User).where(User.id == user_id))
        if not user:
            raise Exception  # TODO: доделать ошибки

        return user.to_dto()
