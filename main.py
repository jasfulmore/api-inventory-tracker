from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from models import ItemCreate, ItemUpdate
from inventory import Item, inventory_manager
from db import get_db, add_item_db, get_all_items_db, delete_item_db
from models import ItemUpdate

app = FastAPI()
security = HTTPBasic()

def authentication(credentials: HTTPBasicCredentials = Depends(security)):
    username_u = 'username'
    password_u = 'password'

    if credentials.username != username_u or credentials.password != password_u:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return credentials.username



@app.get("/items")
def list_items(username_u: str = Depends(authentication), db=Depends(get_all_items_db)):
    items = get_all_items_db(db)
    for row in items:
        return dict(row)

@app.post("/items")
def adding_items(item: ItemCreate, username_u: str = Depends(authentication), db=Depends(get_db)):
    add_item_db(db, item)
    return {'message': f'Item {item.name} has been added to inventory'}

@app.delete("/items/{item_id}")
def delete_items(item_id: int, username_u: str = Depends(authentication), db=Depends(get_db)):
            item = db.query(Item).filter(Item == item_id).first()

            if not item:
                 raise HTTPException(status_code=404, detail="Item not found")
                 
            return {'message': f'Item {item.id} has been deleted'}
            

    
    
@app.put("/items/{item_id}")
def update_item(item_id: int, payload: ItemUpdate, username_u: str = Depends(authentication), db=Depends(get_db)):
    for item in get_all_items_db(get_db):
        if item.id == item_id:
            if payload.quantity is not None:
                item.quantity = payload.quantity
            if payload.price is not None:
                item.price = payload.price

            replenished = inventory_manager.check_replenish(item_id)
            if replenished:
                return {'message': f'Item {item.name} has been replenished successfully'}
            
            # Update the item in the database
            updated_item = Item(
                id=item_id,
                name=item.name,
                quantity=item.quantity,
                price=item.price,
                reorder_lvl=item.reorder_lvl if hasattr(item, "reorder_lvl") else 10
            )
            add_item_db(get_db, updated_item)  # Assuming add_item_db updates if item exists

            return {'message': f'Item {item.name} has been updated in the database successfully'}
    raise HTTPException(status_code=404, detail="Item not found")




