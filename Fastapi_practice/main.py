from fastapi import FastAPI, HTTPException

app = FastAPI()

# In-memory database for demonstration purposes
fake_db = {}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "item_info": fake_db[item_id]}

@app.post("/items/{item_id}")
def create_item(item_id: int, item_info: str):
    if item_id in fake_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    fake_db[item_id] = item_info
    return {"item_id": item_id, "item_info": item_info}

@app.put("/items/{item_id}")
def update_item(item_id: int, item_info: str):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    fake_db[item_id] = item_info
    return {"item_id": item_id, "item_info": item_info}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in fake_db:
        raise HTTPException(status_code=404, detail="Item not found")
    deleted_item_info = fake_db.pop(item_id)
    return {"item_id": item_id, "deleted_item_info": deleted_item_info}
