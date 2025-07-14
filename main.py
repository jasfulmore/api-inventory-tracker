from fastapi import FastAPI, HTTPException
from models import ItemCreate, ItemUpdate
from inventory import Item, inventory_manager


app = FastAPI()



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
def list_items():
    return inventory_manager.get_all_items()

@app.post("/items")
def adding_items(item: ItemCreate):
    new_item = Item(item.id, item.name, item.quantity, item.price)
    return inventory_manager.add_item(new_item)

@app.delete("/items/{item_id}")
def delete_items(item_id):
    for item in inventory_manager.get_all_items():
        if item.id == item.id:
            inventory_manager.items.remove(item)
            print(f'Item {item.id} has been deleted')
            
    raise HTTPException(status_code=404, detail="Item Not Found")
    
    
@app.put("/items/{item_id}")
def update_item(item_id: str, payload: ItemUpdate):
    for item in inventory_manager.get_all_items():
        if item.id == item.id:
            if payload.quantity is not None:
                item.quantity = payload
            elif payload.quantity is not None:
                item.price = payload
            return f'message: Item {item.name} has been updated successfully'

    raise HTTPException(status_code=404, detail="Item not found")



