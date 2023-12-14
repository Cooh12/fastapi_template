from typing import Annotated

from fastapi import Depends

from src.api.providers.uow import uow_provider
from src.infrastructure.db.unit_of_work import SqlAlchemyUnitOfWork

UOW = Annotated[SqlAlchemyUnitOfWork, Depends(uow_provider)]
