import json
import os

def load_inventory(filename="inventory.json"):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                inventory = json.load(file)
                print("Inventory loaded successfully.")
                return inventory
        except json.JSONDecodeError:
            print("Error: Inventory file is corrupted. Starting with empty inventory.")
    else:
        print("No inventory file found. Starting with empty inventory.")
    return {}

def display_menu():
    print("\nInventory System Menu:")
    print("1. View all items")
    print("2. Add an item")
    print("3. Delete an item")
    print("4. Quit")
    print("5. Search for an item")
    print("6. Update item quantity")
    print("7. Clear inventory")
    print("8. Find low stock items")
    print("9. Count items")
    print("10. Summarize inventory")

def view_inventory(inventory):
    if not inventory:
        print("No items in inventory.")
    else:
        print("\nInventory:")
        for i, (name, quantity) in enumerate(inventory.items(), 1):
            print(f"{i}. {name} (Quantity: {quantity})")  

def add_item(inventory, name, quantity, price):
    try:
        if not name.strip():
            raise ValueError("Item name cannot be empty.")
        if not name.replace(" ", "").isalpha():
            raise ValueError("Item name must contain only letters and spaces.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        if not (isinstance(price, float) or isinstance(price, int)) or price <= 0:
            raise ValueError("Price must be a positive number.")

        # Replace this line:
        # if name.lower() in (key.lower() for key in inventory):

        # With this safer version:
        if name.lower() in (key.lower() for key in inventory if isinstance(key, str)):
            print(f"Item {name} already exists!")
            return False

        inventory[name] = {"quantity": quantity, "price": float(price)}
        print(f"Added {name} with quantity {quantity} and price ${price:.2f}.")
        return True
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

def delete_item(inventory, name):
    try:
        for key in list(inventory.keys()):
            if key.lower() == name.lower():
                del inventory[key]
                print(f"Deleted {name}.")
                return True
        print(f"Item {name} not found.")
        return False
    except TypeError:
        print("Error: Invalid input type.")
        return False

def search_item(inventory, name):
    try:
        for key, data in inventory.items():
            if key.lower() == name.lower():
                quantity = data.get("quantity", 0)
                price = data.get("price", 0.0)
                print(f"Found: {key} (Quantity: {quantity}, Price: ${price:.2f})")
                return (key, data)
        print(f"Item {name} not found.")
        return None
    except TypeError:
        print("Error: Invalid input type.")
        return None

def update_item(inventory, name, quantity):
    try:
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        for key in inventory:
            if key.lower() == name.lower():
                inventory[key]["quantity"] = quantity
                print(f"Updated {key} to quantity {quantity}.")
                return True
        print(f"Item {name} not found.")
        return False
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return False

def clear_inventory(inventory):
    try:
        if not inventory:
            print("Inventory is already empty.")
            return False
        inventory.clear()
        print("Inventory cleared.")
        return True
    except TypeError:
        print("Error: Invalid inventory data.")
        return False

def find_low_stock(inventory, threshold):
    try:
        if not isinstance(threshold, int) or threshold < 0:
            raise ValueError("Threshold must be a non-negative number.")
        low_stock = [(name, data["quantity"]) for name, data in inventory.items() if data["quantity"] <= threshold]
        if not low_stock:
            print(f"No items with quantity at or below {threshold}.")
        else:
            print(f"\nLow stock items (quantity <= {threshold}):")
            for i, (name, quantity) in enumerate(low_stock, 1):
                print(f"{i}. {name} (Quantity: {quantity})")
        return low_stock
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")
        return []

def save_inventory(inventory, filename="inventory.json"):
    try:
        with open(filename, "w") as file:
            json.dump(inventory, file, indent=4)
        print(f"Inventory saved to {filename}.")
        return True
    except IOError as e:
        print(f"Error saving inventory: {e}")
        return False
    except TypeError as e:
        print(f"Error: Invalid inventory data: {e}")
        return False

def count_items(inventory):
    try:
        num_items = len(inventory)
        total_quantity = sum(data["quantity"] for data in inventory.values())
        print(f"Inventory summary: {num_items} unique items, total quantity: {total_quantity}")
        return (num_items, total_quantity)
    except Exception as e:
        print(f"Error counting items: {e}")
        return (0, 0)

def summarize_inventory(inventory):
    return count_items(inventory)

