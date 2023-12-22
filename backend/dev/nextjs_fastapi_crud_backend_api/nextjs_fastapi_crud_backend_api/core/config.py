from starlette.config import Config

PROJECT_NAME = "nextjs_fastapi_crud_backend_api"
VERSION = "0.0.1"


config = Config(".env.dev")
DB_USER = config("DB_USER", cast=str)
DB_PASSWORD = config("DB_PASSWORD", cast=str)
DB_HOST = config("DB_HOST", cast=str)
DB_PORT = config("DB_PORT", cast=str)
DB_NAME = config("DB_NAME", cast=str)


MYSQL_SQLALCHEMY_DATABASE_URI = config(
    "MYSQL_SQLALCHEMY_DATABASE_URI",
    default=f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)

AIOMYSQL_SQLALCHEMY_DATABASE_URI = config(
    "AIOMYSQL_SQLALCHEMY_DATABASE_URI",
    default=f"mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
)
