# 📦 API Inventory Tracker

A lightweight and extensible Python-based inventory management API designed to help manage items, quantities, and pricing. Built for learning, testing, or expanding into a full-featured inventory system.

## 🚀 Features

- 📘 Item management (ID, name, quantity, price)
- 🔄 CRUD operations for inventory items
- 🧮 Total inventory valuation
- 🧪 Easily testable Python structure
- 💡 Clear object-oriented design using `Item` and `InventoryManager` classes

## 🧠 Skills & Technologies Used

- **Python 3** — Core language for logic and object-oriented structure
- **OOP (Object-Oriented Programming)** — Class-based design for managing inventory
- **Git & GitHub** — Version control and collaboration
- **Unit Testing (basic)** — Sample test file for validating core functions
- **CLI Scripting** — Simple terminal-based inventory management
- **API Endpoints** for CRUD operations

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
