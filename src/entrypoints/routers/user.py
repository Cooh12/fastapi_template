from fastapi import APIRouter

from src.application import dto
from src.entrypoints.providers.schemas import UOW
from src.infrastructure import service_layer

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/{user_id}')
async def get_by_id(user_id: int, uow: UOW):
    return await service_layer.get_user_by_id(dto.UserId(user_id), uow)
