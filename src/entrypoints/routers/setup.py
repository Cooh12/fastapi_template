from fastapi import FastAPI

from src.entrypoints.routers.user import user_router


def setup_routes(app: FastAPI) -> None:
    app.include_router(user_router)
