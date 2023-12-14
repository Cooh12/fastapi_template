from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column, registry

from src.application import dto
from .base import TimedBaseModel

mapper_registry = registry()


class User(TimedBaseModel):
    __tablename__ = "users"
    __mapper_args__ = {"eager_defaults": True}

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    username: Mapped[str | None] = mapped_column(unique=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    middle_name: Mapped[str | None]
    deleted_at: Mapped[datetime | None] = mapped_column(default=None, server_default=sa.Null())

    def to_dto(self) -> dto.User:
        return dto.User(
            id=dto.UserId(self.id),
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name,
            middle_name=self.last_name,
        )
