from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from nextjs_fastapi_crud_backend_api.core.config import (
    MYSQL_SQLALCHEMY_DATABASE_URI,
    AIOMYSQL_SQLALCHEMY_DATABASE_URI,
)
import logging
from fastapi import FastAPI

logger = logging.getLogger(__name__)

# engine = create_engine(MYSQL_SQLALCHEMY_DATABASE_URI)
engine = create_async_engine(AIOMYSQL_SQLALCHEMY_DATABASE_URI, echo=True)

async_session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)

Base = declarative_base()

# Base.metadata.create_all(bind=engine)


async def connect_to_db(app: FastAPI) -> None:
    try:
        db = async_session()
        app.state._db = db
    except Exception as e:
        logger.warn("--- DATABASE CONNECTION ERROR ---")
        logger.warn(e)
        logger.warn("--- DATABASE CONNECTION ERROR ---")


async def close_db_connection(app: FastAPI) -> None:
    try:
        await app.state._db.close()
    except Exception as e:
        logger.warn("--- DATABASE DISCONNECT ERROR ---")
        logger.warn(e)
        logger.warn("--- DATABASE DISCONNECT ERROR ---")
