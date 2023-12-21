import asyncio

from src.api.config import Config
from src.api.factory import run_api, init_api
from src.infrastructure.config_loader import load_config
from src.infrastructure.db.factory import build_sa_session_factory, build_sa_engine


async def main() -> None:
    config = load_config(Config)
    engine = await build_sa_engine(config.db)
    pool = build_sa_session_factory(engine)
    app = init_api(pool)
    try:
        await run_api(app, config.api)
    finally:
        await engine.dispose()


if __name__ == '__main__':
    asyncio.run(main())
