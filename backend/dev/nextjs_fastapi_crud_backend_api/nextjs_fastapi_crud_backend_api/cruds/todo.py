from sqlalchemy.ext.asyncio import AsyncSession

from nextjs_fastapi_crud_backend_api.models.todo import Item
from nextjs_fastapi_crud_backend_api.schemas.todo import ItemCreate
from datetime import datetime


async def create_item(db: AsyncSession, request) -> Item:
    current_time = datetime.now()
    item = Item(
        name=request.name,
        contents=request.contents,
    )
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item
