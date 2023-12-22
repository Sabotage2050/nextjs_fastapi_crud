from fastapi import Depends, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from nextjs_fastapi_crud_backend_api.schemas.todo import (
    ItemCreate,
    ItemRequest,
    ItemResponse,
)
from nextjs_fastapi_crud_backend_api.models.todo import Item
from nextjs_fastapi_crud_backend_api.dependencies.todo import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from nextjs_fastapi_crud_backend_api.cruds.todo import create_item

router = APIRouter()


# GetAllItem
@router.get("/items", response_model=List[ItemResponse])
def get_items(
    db: AsyncSession = Depends(get_db),
):
    result_set: List[Item] = db.query(Item).all()
    return [ItemResponse(name=item.name, contents=item.contents) for item in result_set]
    # response_body = jsonable_encoder(result_set)
    # return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# GetItem
@router.get("/item/{id}", response_model=ItemResponse)
def get_item(id: int, db: AsyncSession = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    # response_body = jsonable_encoder(item)
    # return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)
    return ItemResponse(name=item.name, contents=item.contents)


# CreateItem
@router.post("/item", response_model=ItemCreate)
async def a_create_item(request: ItemRequest, db: AsyncSession = Depends(get_db)):
    res = await create_item(db,request)
    return ItemCreate(id=res.item_id)
    # response_body = jsonable_encoder({"item_id": item.item_id})
    # return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# UpdateItem
@router.put("/item/{id}", response_model=ItemCreate)
def update_item(id: int, request: ItemRequest, db: AsyncSession = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    item.name = request.name
    item.contents = request.contents
    db.commit()
    return ItemCreate(id=item.item_id)
    # item = jsonable_encoder(item)
    # return JSONResponse(status_code=status.HTTP_200_OK, content=item)


# DeleteItem
@router.delete("/item/{id}", response_model=None)
def delete_item(id: int, db: AsyncSession = Depends(get_db)):
    db.query(Item).filter(Item.item_id == id).delete()
    db.commit()
    # return JSONResponse(status_code=status.HTTP_200_OK, content="ok")
    return
