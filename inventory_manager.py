# inventory_manager
import threading


class InventoryManager:
    def __init__(self):
        self.inventory = []
        self.lock = threading.Lock()

    def add_item(self, item):
        with self.lock:
            self.inventory.append(item)
            print(f"Added to inventory: {item}")

    def generate_items(self, item_type, attributes, count, factory):
        base_item = factory.create_item(item_type, **attributes)
        self.add_item(base_item)
        for _ in range(count - 1):
            cloned_item = base_item.clone()
            self.add_item(cloned_item)

    def show_inventory(self):
        with self.lock:
            print("\nCurrent Inventory:")
            for item in self.inventory:
                print(item)
            print("-" * 30)
