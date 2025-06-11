import json

inventory = {"Apple": 10, "Banana": 5}
print(f"[DEBUG] Saving inventory: {inventory}")
with open("Inventory.json", "w") as file:
    json.dump(inventory, file, indent=4)
print("Done saving")