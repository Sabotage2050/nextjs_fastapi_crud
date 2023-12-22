from sqlalchemy.ext.asyncio import AsyncSession
from starlette.requests import Request
from nextjs_fastapi_crud_backend_api.db.todo import async_session


async def get_db(request: Request) -> AsyncSession:
    return request.app.state._db
