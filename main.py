# main.py
import threading
from inventory_manager import InventoryManager
from inventory_item import ItemFactory


if __name__ == "__main__":
    inventory_manager = InventoryManager()
    factory = ItemFactory()

    thread1 = threading.Thread(target=inventory_manager.generate_items, args=(
        'Desk', {'height': 75, 'material': 'wood', 'type': 'pupil'}, 3, factory))

    thread2 = threading.Thread(target=inventory_manager.generate_items, args=(
        'Desktop', {'processor': 'Intel i5', 'RAM': 16, 'type': 'workstation'}, 3, factory))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    base_desk = factory.create_item('Desk', **{'height': 75, 'material': 'wood', 'type': 'pupil'})
    desk_for_teacher = base_desk.clone(type='teacher')
    inventory_manager.add_item(desk_for_teacher)

    inventory_manager.show_inventory()
