from typing import Annotated

from fastapi import Depends

from src.entrypoints.providers.uow import uow_provider
from src.infrastructure.service_layer.unit_of_work import SqlAlchemyUnitOfWork

UOW = Annotated[SqlAlchemyUnitOfWork, Depends(uow_provider)]
