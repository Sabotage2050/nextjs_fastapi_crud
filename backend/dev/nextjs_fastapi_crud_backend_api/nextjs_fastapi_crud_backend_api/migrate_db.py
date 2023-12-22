from sqlalchemy import create_engine

from nextjs_fastapi_crud_backend_api.core.config import MYSQL_SQLALCHEMY_DATABASE_URI
from nextjs_fastapi_crud_backend_api.models.todo import Base

engine = create_engine(MYSQL_SQLALCHEMY_DATABASE_URI, echo=True)


def reset_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    reset_database()