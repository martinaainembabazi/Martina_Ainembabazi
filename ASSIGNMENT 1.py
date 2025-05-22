# Simple Inventory Management System

inventorylist = {
    "Milk":200,
    "TraysofEggs":80,
    "Soda":50,
    "Sugar":100,
    "Bread":40,
    "Butter": 30,
    "Rice":150,
    "Flour": 120
    }
inventory={}
for item, qty in inventorylist:
    inventory[item] = qty

while True:
    print("\nInventory Management")
    print("1. Add/Update Item")
    print("2. Remove Item")
    print("3. View Inventory")
    print("4. Exit")
    option = input("Enter your an option (1-4): ")

    if option == '1':
        item = input("Enter item name: ")
        qty = int(input("Enter quantity: "))
        if item in inventory:
            inventory[item] += qty
            print(f"Updated {item} quantity to {inventory[item]}")
        else:
            inventory[item] = qty
            print(f"Added {item} with quantity {qty}")
    elif option == '2':
        item = input("Enter item name to remove: ")
        if item in inventory:
            del inventory[item]
            print(f"Removed {item} from inventory.")
        else:
            print("Item not found.")
    elif option == '3':
        print("\nCurrent Inventory:")
        if not inventory:
            print("Inventory is empty.")
        else:
            for item, qty in inventory.items():
                print(f"{item}: {qty}")
    elif option == '4':
        print("Exiting Inventory Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
