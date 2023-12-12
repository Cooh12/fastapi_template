import uvicorn
from fastapi import FastAPI
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.entrypoints.providers.main import setup_providers
from src.entrypoints.routers.setup import setup_routes


def init_api(pool: async_sessionmaker[AsyncSession]) -> FastAPI:
    app = FastAPI()
    setup_providers(app, pool)
    setup_routes(app)
    return app


async def run_api(app: FastAPI):
    config = uvicorn.Config(app)
    server = uvicorn.Server(config)
    await server.serve()
