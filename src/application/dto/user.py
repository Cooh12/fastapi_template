from dataclasses import dataclass, field
from typing import NewType

UserId = NewType('UserId', int)


@dataclass(frozen=True)
class User:
    id: UserId | None
    username: str
    first_name: str
    last_name: str
    middle_name: str | None
    deleted_at: None = field(default=None, init=False)
