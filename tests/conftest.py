import logging
import os
from typing import Generator, AsyncGenerator

import orjson
import pytest
import pytest_asyncio
from alembic.command import upgrade
from alembic.config import Config as AlembicConfig
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession, create_async_engine
from sqlalchemy_utils import database_exists, drop_database, create_database
from testcontainers.postgres import PostgresContainer

logger = logging.getLogger(__name__)


@pytest.fixture(scope='session')
def postgres_url() -> Generator[str, None, None]:
    postgres = PostgresContainer(dbname='reference_db')
    if os.name == 'nt':  # TODO: workaround from testcontainers/testcontainers-python#108
        postgres.get_container_host_ip = lambda: 'localhost'
    try:
        postgres.start()
        postgres_url_ = postgres.get_connection_url().replace('psycopg2', 'asyncpg')
        logger.info('postgres url %s', postgres_url_)
        yield postgres_url_
    finally:
        postgres.stop()


@pytest.fixture(scope='session')
def alembic_config(postgres_url: str) -> AlembicConfig:
    alembic_cfg = AlembicConfig('alembic.ini')
    alembic_cfg.set_main_option('sqlalchemy.url', postgres_url)
    return alembic_cfg


@pytest.fixture(scope='session', autouse=True)
def upgrade_schema_db(alembic_config: AlembicConfig) -> None:
    upgrade(alembic_config, 'head')


@pytest_asyncio.fixture
async def session_factory(postgres_url: str) -> AsyncGenerator[async_sessionmaker[AsyncSession], None]:
    test_url_async = postgres_url.replace('reference_db', 'test_db')
    test_url_sync = test_url_async.replace('asyncpg', 'psycopg2')

    if database_exists(test_url_sync):
        drop_database(test_url_sync)
    create_database(test_url_sync, template='reference_db')

    engine = create_async_engine(
        url=test_url_async,
        json_serializer=lambda data: orjson.dumps(data).decode(),
        json_deserializer=orjson.loads,
    )
    session_factory_: async_sessionmaker[AsyncSession] = async_sessionmaker(
        bind=engine, expire_on_commit=False, autoflush=False
    )
    yield session_factory_
    await engine.dispose()


@pytest_asyncio.fixture
async def session(session_factory: async_sessionmaker[AsyncSession]) -> AsyncGenerator[AsyncSession, None]:
    async with session_factory() as session_:
        yield session_
