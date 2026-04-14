from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.post("/items/")
async def create_item(item: Item):
    return item

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": "Sample Item", "price": 10.0}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "name": item.name, "price": item.price}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "message": "Item deleted"}

