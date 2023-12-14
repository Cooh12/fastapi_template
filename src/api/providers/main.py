from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from src.api.providers.uow import UnitOfWorkProvider, uow_provider


def setup_providers(app: FastAPI, pool: async_sessionmaker[AsyncSession]) -> None:
    uow_provider_ = UnitOfWorkProvider(pool)

    app.dependency_overrides[uow_provider] = uow_provider_.uow
