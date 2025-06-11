import inventory_mod

# Load the inventory from the JSON file
inventory = inventory_mod.load_inventory()

while True:
    inventory_mod.display_menu()
    choice = input("Enter your choice: ")

    match choice:
        case "1":  # View all items
            print("Debug Inventory:", inventory)
            inventory_mod.view_inventory(inventory)
            

        case "2":  # Add an item
            name = input("Enter item name: ")
            try:
                quantity = int(input("Enter quantity: "))
                price = float(input("Enter price: "))
                inventory_mod.add_item(inventory, name, quantity, price)
                inventory_mod.save_inventory(inventory)
            except ValueError:
                print("Invalid input. Quantity must be an integer and price must be a number.")
                

        case "3":  # Delete an item
            name = input("Enter item name to delete: ")
            inventory_mod.delete_item(inventory, name)
            inventory_mod.save_inventory(inventory)

        case "4":  # Quit
            inventory_mod.save_inventory(inventory)
            print("Goodbye!")
            break

        case "5":  # Search for an item
            name = input("Enter item name to search: ")
            inventory_mod.search_item(inventory, name)

        case "6":  # Update item quantity
            name = input("Enter item name to update: ")
            try:
                quantity = int(input("Enter new quantity: "))
                inventory_mod.update_item(inventory, name, quantity)
            except ValueError:
                print("Quantity must be a positive integer.")
                inventory_mod.save_inventory(inventory)

        case "7":  # Clear inventory
            confirm = input("Are you sure you want to clear the inventory? (yes/no): ").lower()
            if confirm == "yes":
                inventory_mod.clear_inventory(inventory)
                inventory_mod.save_inventory(inventory)

        case "8":  # Find low stock items
            try:
                threshold = int(input("Enter low stock threshold: "))
                inventory_mod.find_low_stock(inventory, threshold)
            except ValueError:
                print("Threshold must be a non-negative integer.")

        case "9":  # Count items
            inventory_mod.count_items(inventory)

        case "10":  # Summarize inventory (same as count)
            inventory_mod.summarize_inventory(inventory)

        case _:  # Default fallback
            print("Invalid choice. Please enter a number between 1 and 10.")