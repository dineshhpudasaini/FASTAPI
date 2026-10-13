
from fastapi import FastAPI

app = FastAPI()

# CREATE
@app.post("/items")
def create_item():
    return {"message": "Created"}


# READ
@app.get("/items")
def read_items():
    return {"message": "Read all items"}


# READ ONE
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


# UPDATE
@app.put("/items/{item_id}")
def update_item(item_id: int):
    return {"message": "Updated", "id": item_id}


# PARTIAL UPDATE
@app.patch("/items/{item_id}")
def patch_item(item_id: int):
    return {"message": "Partially updated", "id": item_id}


# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": "Deleted", "id": item_id}
