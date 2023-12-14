from src.application import dto
from src.application.interfaces.user import UserAdapters


class UserFakeRepository(UserAdapters):
    users = set()

    async def add(self, user: dto.User) -> None:
        self.users.add(user)

    async def get_by_id(self, user_id: dto.UserId) -> dto.User:
        return next((p for p in self.users if p.id == user_id), None)
