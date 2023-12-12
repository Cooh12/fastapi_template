from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker, AsyncSession


def build_sa_session_factory(engine: AsyncEngine) -> async_sessionmaker[AsyncSession]:
    session_factory = async_sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)
    return session_factory
