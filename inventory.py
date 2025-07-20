class Item:
    def __init__(self, id: int, name: str, quantity: int, price: float, reorder_lvl: int):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.reorder_lvl = reorder_lvl

    def __repr__(self):
        return f'(\nid = {self.id}\nname = {self.name}\nquantity = {self.quantity}\nprices = ${self.price:.2f}\n)'
    

class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        print('Before add:', self.items)
        self.items.append(item)
        print('After add:', self.items)
        return {'Item': f'Item {item.name} has been added to inventory.'}
    
    def get_all_items(self):
        return self.items   
    
    def check_replenish(self, item_id):
        for item in self.items:
            if item.id == item_id:
                if item.quantity < item.reorder_lvl:
                    item.quantity += 10000
                    return {'message': f'Item {item.name} was below reorder threshold and has been replenished to {item.quantity} units'}
                else:
                    return {'message': f'Item {item.name} does not to be replenished.\nCurrent Quant: {item.quantity}.'}
        return {'message': 'Item not found'}
            



inventory_manager = InventoryManager()
item1 = Item(1, 'Macbook Pro', 234, 1900, 10)
inventory_manager.add_item(item1)

