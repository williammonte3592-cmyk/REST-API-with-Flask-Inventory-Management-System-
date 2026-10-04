# Summative-Lab-Python-REST-API-with-Flask--Inventory-Management-System-

A Flask REST API for managing inventory with a command-line interface.

## Quick Start

```bash
# Install dependencies
pipenv install

# Run Flask server
cd inventory_system
python app.py

# In another terminal, run CLI
cd inventory_system
python cli.py

When you run python cli.py, you will see:
text
1. View all      # Shows all items in inventory
2. Add item      # Adds new item (name, price, stock)
3. Exit          # Closes the CLI
Choice: _
Run Tests
bash
pytest inventory_system/test_app.py -v
API Endpoints
Method	Endpoint	Description
GET	/inventory	View all items
GET	/inventory/1	View one item
POST	/inventory	Add item
PATCH	/inventory/1	Update item
DELETE	/inventory/1	Delete item
GET	/fetch/5449000000996	Search OpenFoodFacts

Example
Add an item:

text
Choice: 2
Name: Macbook Pro
Price: 2390
Stock: 1
Added! ID: 1
View all items:

text
Choice: 1
1: Macbook Pro - $2390.0 - stock:1


#Project Structure
text
inventory_system/
├── app.py
├── cli.py
└── test_app.py
Pipfile
README.md
LICENSE
Built With
Flask

Requests

Pytest

OpenFoodFacts API



OpenFoodFacts API