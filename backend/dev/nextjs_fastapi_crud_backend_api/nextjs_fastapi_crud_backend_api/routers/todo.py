from fastapi import Depends, status, APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from nextjs_fastapi_crud_backend_api.schemas.todo import ItemRequest
from nextjs_fastapi_crud_backend_api.models.todo import Item
from nextjs_fastapi_crud_backend_api.dependencies.todo import get_db
from sqlalchemy.orm import Session
from nextjs_fastapi_crud_backend_api.schemas.todo import ItemResponse,ItemRequest
from typing import List

router = APIRouter()

# GetAllItem
@router.get("/items",response_model=List[ItemResponse])
def get_items(
    db: Session = Depends(get_db),
):
    result_set = db.query(Item).all()
    response_body = jsonable_encoder(result_set)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# GetItem
@router.get("/item/{id}")
def get_item(id: int, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    response_body = jsonable_encoder(item)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# CreateItem
@router.post("/item")
def create_item(request: ItemRequest, db: Session = Depends(get_db)):
    item = Item(name=request.name, contents=request.contents)
    db.add(item)
    db.commit()
    response_body = jsonable_encoder({"item_id": item.item_id})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# UpdateItem
@router.put("/item/{id}")
def update_item(id: int, request: ItemRequest, db: Session = Depends(get_db)):
    item = db.query(Item).filter(Item.item_id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    item.name = request.name
    item.contents = request.contents
    db.commit()
    item = jsonable_encoder(item)
    return JSONResponse(status_code=status.HTTP_200_OK, content=item)


# DeleteItem
@router.delete("/item/{id}")
def delete_item(id: int, db: Session = Depends(get_db)):
    db.query(Item).filter(Item.item_id == id).delete()
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content="ok")