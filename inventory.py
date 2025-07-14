class Item:
    def __init__(self, id: int, name: str, quantity: int, price: float):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f'(\nid = {self.id}\nname = {self.name}\nquantity = {self.quantity}\nprices = ${self.price:.2f}\n)'
    

class InventoryManager:
    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        print('Before add:', self.items)
        self.items.append(item)
        print('After add:', self.items)
        return f'Item {item.name} has been added to inventory.'
    
    def get_all_items(self):
        return self.items   
            



inventory_manager = InventoryManager()
item1 = Item(1, 'Macbook Pro', 234, 1900)
inventory_manager.add_item(item1)

