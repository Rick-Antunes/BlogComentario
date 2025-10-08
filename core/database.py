from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine

from sqlalchemy.orm.session import sessionmaker
from core.configs import settings

<<<<<<< HEAD
=======

>>>>>>> 689446a (first commit)
engine: AsyncEngine = create_async_engine(settings.DB_URL)
Session: AsyncSession = sessionmaker(
    autoflush=False,
    autocommit=False,
    expire_on_commit=False,
    class_=AsyncSession,
    bind=engine
)