from sqlalchemy import Column, Integer, String
from sqlalchemy import DateTime, func
from nextjs_fastapi_crud_backend_api.db.todo import Base

# Entity Item
class Item(Base):
    __tablename__ = "item"
    item_id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    contents = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())





