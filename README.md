# 📦 API Inventory Tracker

A lightweight and extensible Python-based inventory management API designed to help manage items, quantities, and pricing. Built for learning, testing, or expanding into a full-featured inventory system.

## 🚀 Features

- 📘 Item management (ID, name, quantity, price)
- 🔄 CRUD operations for inventory items
- 🧮 Total inventory valuation
- 🧪 Easily testable Python structure
- 💡 Clear object-oriented design using `Item` and `InventoryManager` classes

## 🧠 Skills & Technologies Used
- **Language**: Python 3.x
- **Framework**: FastAPI – for building the RESTful API
- **Database**: SQLite – lightweight relational database for persistence
- **ORM**: SQLAlchemy – used to interact with the SQLite database
- **Pydantic**: for data validation and serialization
- **Uvicorn**: ASGI server used to run the FastAPI app
- **Swagger UI**: automatically generated docs at /docs
- **Git**: version control for tracking project changes
- **JSON**: used for testing and exchanging structured data (via Swagger)


## 🛠️ Getting Started

### Prerequisites

- Python 3.8+
- `pip` for installing dependencies (if any in the future)

### Clone the Repository

```bash
git clone https://github.com/jasfulmore/api-inventory-tracker.git
cd api-inventory-tracker
````

### Run the Inventory Tracker

```bash
python inventory.py
```

You can modify the script to add, update, or delete items using the `InventoryManager` class methods.

## 🧪 Example Usage

```python
from inventory import Item, InventoryManager

manager = InventoryManager()

# Add new items
manager.add_item(Item(1, 'Mouse', 10, 25.99))
manager.add_item(Item(2, 'Keyboard', 5, 45.50))

# Update item
manager.update_item(1, quantity=15)

# Display inventory
manager.display_inventory()

# Calculate total value
print(f"Total Inventory Value: ${manager.total_value():.2f}")
```

## ✅ To-Do / Ideas for Expansion

* [ ] Add Flask API endpoints
* [X] Implement SQLite or PostgreSQL backend
* [ ] Add user authentication
* [ ] Create a frontend dashboard (React or plain HTML/CSS)

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first to discuss what you'd like to change or improve.

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

> Built with 💻 by [Jas Fulmore](https://github.com/jasfulmore)
