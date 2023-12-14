from fastapi import APIRouter

from src.api import service_layer
from src.api.providers.schemas import UOW
from src.application import dto

user_router = APIRouter(prefix='/users', tags=['Users'])


@user_router.get('/{user_id}')
async def get_by_id(user_id: int, uow: UOW) -> dto.User:
    return await service_layer.get_user_by_id(dto.UserId(user_id), uow)
