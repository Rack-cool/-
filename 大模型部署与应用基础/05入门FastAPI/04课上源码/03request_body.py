from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    descroption: str=None
    width: float
    height: float

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.post("/items/{item_id}")
async def modify_item(item_id: int, item:Item):
    return {"item_id": item_id, **item.dict()}


