# inventory_item.py
import copy


class InventoryItem:
    def __init__(self, name, **attributes):
        self.name = name
        self.attributes = attributes
        self.inventory_id = InventoryIDGenerator().generate_id()

    def clone(self, **new_attributes):
        cloned_item = copy.deepcopy(self)
        cloned_item.attributes.update(new_attributes)
        cloned_item.inventory_id = InventoryIDGenerator().generate_id()
        return cloned_item

    def __str__(self):
        attr_str = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
        return f"ID: {self.inventory_id}, {self.name} ({attr_str})"


class InventoryIDGenerator:
    _instance = None
    _id = 0

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryIDGenerator, cls).__new__(cls)
        return cls._instance

    def generate_id(self):
        self._id += 1
        return self._id


class ItemFactory:
    @staticmethod
    def create_item(item_type, **attributes):
        return InventoryItem(item_type, **attributes)
