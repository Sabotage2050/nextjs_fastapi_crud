from pydantic import BaseModel, Field


class ItemBase(BaseModel):
    name: str = Field(..., max_length=50)
    contents: str = Field(..., max_length=100)
class ItemRequest(ItemBase):
    pass

class ItemResponse(ItemBase):
    pass

class ItemCreate(BaseModel):
    id: int = Field(..., ge=1)