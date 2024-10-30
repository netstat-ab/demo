from typing import cast

from sqlalchemy import Engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.pool import NullPool, AsyncAdaptedQueuePool
from .settings import settings, Environment

# DB_POOL_SIZE = 83
# WEB_CONCURRENCY = 9
# POOL_SIZE = max(DB_POOL_SIZE // WEB_CONCURRENCY, 5)

# connect_args = {"check_same_thread": False}

engine = create_async_engine(
    str(settings.ASYNC_DATABASE_URI),
    echo=False,
    poolclass=NullPool if settings.ENV == Environment.TEST else AsyncAdaptedQueuePool,
    # pool_size=POOL_SIZE,
    # max_overflow=64,
)

SessionLocal = sessionmaker(
    bind=cast(Engine, engine),
    autocommit=False,
    autoflush=False,
    class_=AsyncSession,
    expire_on_commit=False,
)


# engine_celery = create_async_engine(
#     str(settings.ASYNC_CELERY_BEAT_DATABASE_URI),
#     echo=False,
#     poolclass=NullPool
#     if settings.MODE == ModeEnum.testing
#     else AsyncAdaptedQueuePool,  # Asincio pytest works with NullPool
#     pool_size=POOL_SIZE,
#     max_overflow=64,
# )

# SessionLocalCelery = sessionmaker(
#     autocommit=False,
#     autoflush=False,
#     bind=engine_celery,
#     class_=AsyncSession,
#     expire_on_commit=False,
# )
