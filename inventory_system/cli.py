import requests

BASE = "http://127.0.0.1:5555"

while True:
    print("\n1. View all")
    print("2. Add item")
    print("3. Exit")
    choice = input("Choice: ")
    
    if choice == '1':
        r = requests.get(f"{BASE}/inventory")
        print(r.json())
    
    elif choice == '2':
        name = input("Name: ")
        price = float(input("Price: "))
        stock = int(input("Stock: "))
        r = requests.post(f"{BASE}/inventory", json={"name": name, "price": price, "stock": stock})
        print("Added!", r.json())
    
    elif choice == '3':
        break