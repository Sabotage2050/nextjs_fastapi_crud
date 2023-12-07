from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import FetchedValue
from sqlalchemy import create_engine
from starlette.middleware.cors import CORSMiddleware
import os
from fastapi import FastAPI, Depends, Query, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import DateTime, func

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Change this to the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    os.environ.get("DB_USER"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("DB_HOST"),
    os.environ.get("DB_PORT"),
    os.environ.get("DB_NAME"),
)

engine = create_engine(SQLALCHEMY_DATABASE_URI)


Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def session():
    db = Session()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base(bind=engine)


# Entity Item
class Item(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    contents = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


Base.metadata.create_all(bind=engine)


# Request Body
class ItemRequest(BaseModel):
    name: str = Query(..., max_length=50)
    contents: str = Query(..., max_length=100)


# GetAllItem
@app.get("/items")
def get_items(
    db: Session = Depends(session),
):
    result_set = db.query(Item).all()
    response_body = jsonable_encoder(result_set)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# GetItem
@app.get("/item/{id}")
def get_item(id: int, db: Session = Depends(session)):
    item = db.query(Item).filter(Item.item_id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    response_body = jsonable_encoder(item)
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# CreateItem
@app.post("/item")
def create_item(request: ItemRequest, db: Session = Depends(session)):
    item = Item(name=request.name, contents=request.contents)
    db.add(item)
    db.commit()
    response_body = jsonable_encoder({"item_id": item.item_id})
    return JSONResponse(status_code=status.HTTP_200_OK, content=response_body)


# UpdateItem
@app.put("/item/{id}")
def update_item(id: int, request: ItemRequest, db: Session = Depends(session)):
    item = db.query(Item).filter(Item.item_id == id).first()
    if item is None:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)
    item.name = request.name
    item.contents = request.contents
    db.commit()
    item = jsonable_encoder(item)
    return JSONResponse(status_code=status.HTTP_200_OK, content=item)


# DeleteItem
@app.delete("/item/{id}")
def delete_item(id: int, db: Session = Depends(session)):
    db.query(Item).filter(Item.item_id == id).delete()
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content="ok")
