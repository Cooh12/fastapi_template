import logging

import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.api.config import APIConfig
from src.api.providers.main import setup_providers
from src.api.routers.setup import setup_routes


def init_api(pool: async_sessionmaker[AsyncSession]) -> FastAPI:
    app = FastAPI()
    setup_providers(app, pool)
    setup_routes(app)
    return app


async def run_api(app: FastAPI, api_config: APIConfig):
    config = uvicorn.Config(
        app,
        port=api_config.port,
        host=api_config.host,
        log_level=logging.INFO,
    )
    server = uvicorn.Server(config)
    await server.serve()
