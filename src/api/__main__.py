import asyncio

from sqlalchemy.ext.asyncio import create_async_engine

from src.api.factory import run_api, init_api
from src.infrastructure.db.main import build_sa_session_factory


async def main() -> None:
    engine = create_async_engine(url='postgresql+asyncpg://postgres:postgres@localhost:5432/fastapi_template')
    pool = build_sa_session_factory(engine)
    app = init_api(pool)
    try:
        await run_api(app)
    finally:
        await engine.dispose()


if __name__ == '__main__':
    asyncio.run(main())
