from typing import Protocol

from src.application import dto


class UserAdapters(Protocol):
    async def add(self, user: dto.User) -> None:
        raise NotImplementedError

    async def get_by_id(self, user_id: dto.UserId) -> dto.User:
        raise NotImplementedError
