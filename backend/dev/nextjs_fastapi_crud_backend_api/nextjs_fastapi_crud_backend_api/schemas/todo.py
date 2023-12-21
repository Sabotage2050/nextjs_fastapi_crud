from pydantic import BaseModel, Field
from fastapi import Query

# Request Body
class ItemRequest(BaseModel):
    name: str = Query(..., max_length=50)
    contents: str = Query(..., max_length=100)

class ItemResponse(BaseModel):
    name: str = Field(..., max_length=50)
    contents: str = Field(..., max_length=100)