from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from nextjs_fastapi_crud_backend_api.core.config import SQLALCHEMY_DATABASE_URI
import logging
from fastapi import FastAPI

logger = logging.getLogger(__name__)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
 
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
Base = declarative_base(bind=engine)
 
Base.metadata.create_all(bind=engine)

async def connect_to_db(app: FastAPI) -> None:
    try:
        db = session()
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



