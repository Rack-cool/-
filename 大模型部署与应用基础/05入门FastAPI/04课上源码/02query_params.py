from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
async def get_items(skip: int=0, limit:int=10):
    return {"items":[], "skip":skip, "limit":limit}

@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str):
    return {"item_id": item_id, "q": q}


@app.get("/items_bool/{item_id}")
async def get_item(item_id: int, q: str=None, short: bool=False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    item.update({"short": short})
    return item
