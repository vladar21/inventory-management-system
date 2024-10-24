# Overview

Hi!

My name is Vladislav Rastvorov, I am a student of CO.SDH3-A group.

Now I will tell you about my code for the first assignment:

Create an inventory management system using factory and proto design patterns with multithreading for item management using Python.

Ok, first, the general concept of the solution: 

The code implements an ```Inventory Management System``` that dynamically generates inventory items using a combination of the ```Factory Design Pattern``` and ```Prototype Design Pattern```. The system ensures that each item has a unique inventory ID, which is generated using a ```Singleton pattern```. 

Additionally, it incorporates ```multithreading``` to handle concurrent item creation, ensuring thread safety with locks. 

The code is divided into three files:
1) ```inventory_item.py``` - which contains everything you need to create an inventory.
2) ```inventory_manager.py``` - everything you need to manage your inventory.
3) ```main.py``` - demonstration of the code features.

## File: inventory_item.py

1) This imports the Python copy module, which is used to create deep copies of objects. 
```python
import copy
```

2) Defines the InventoryItem class.
```python
class InventoryItem:
```

3) This is the constructor method. It initializes an InventoryItem instance.
```python
def __init__(self, name, **attributes):
    self.name = name
    self.attributes = attributes
    self.inventory_id = InventoryIDGenerator().generate_id()
```

```self.name = name:``` Assigns the name of the item to the instance (e.g., desk, desktop).

```self.attributes = attributes:``` Stores the attributes (such as height, material, etc.) in the attributes variable.

```self.inventory_id = InventoryIDGenerator().generate_id():``` Uses the InventoryIDGenerator class to generate a unique ID for each item. 

4) This method creates a deep copy (clone) of the item.  
```python
def clone(self, **new_attributes):
    cloned_item = copy.deepcopy(self)
    cloned_item.attributes.update(new_attributes)
    cloned_item.inventory_id = InventoryIDGenerator().generate_id()
    return cloned_item
```

```cloned_item = copy.deepcopy(self):``` Creates a deep copy of the current item.

```cloned_item.attributes.update(new_attributes):``` If new attributes are passed, they are added or updated in the cloned item.

```cloned_item.inventory_id = InventoryIDGenerator().generate_id():``` The cloned item gets a new unique inventory ID.

```return cloned_item:``` Returns the cloned item.

5) Defines a string representation of the item.
```python
def __str__(self):
    attr_str = ', '.join(f"{key}: {value}" for key, value in self.attributes.items())
    return f"ID: {self.inventory_id}, {self.name} ({attr_str})"
```
    
When an InventoryItem object is printed, it will display the ID, name, and all of its attributes in a readable format.

6) Defines the InventoryIDGenerator class. This class ensures that every item gets a unique ID, using the Singleton pattern.
```python
class InventoryIDGenerator:
```

7) Static variables
```pytho
_instance = None
_id = 0
```

```_instance = None:``` holds the instance of the class (Singleton).
```_id = 0:``` keeps track of the current ID count.

8) The method ensures that only one instance of the class is created (Singleton pattern)
```python
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(InventoryIDGenerator, cls).__new__(cls)
        return cls._instance
```
```cls:``` Refers to the class itself and is used in class methods or special methods like __new__().

9) This method increments the _id counter (unique inventory number)
```python
def generate_id(self):
    self._id += 1
    return self._id
```
    
10) Factory for creating instances of InventoryItem Class
```python
class ItemFactory:
    @staticmethod
    def create_item(item_type, **attributes):
        return InventoryItem(item_type, **attributes)
```

```@staticmethod:``` This decorator indicates that create_item is a static method.

```create_item(item_type, **attributes):``` Creates and returns a new InventoryItem based on the item_type (e.g., "Desk", "Desktop") and provided attributes (e.g., height, material).


## File: inventory_manager.py

1) The threading module allows for the creation and management of multiple threads.
```python
import threading
```

2) Defines the InventoryManager class, which is responsible for managing inventory items, adding new items, and displaying the current inventory.

```python
class InventoryManager:
```

3) Initializes the InventoryManager instance.

```python
def __init__(self):
    self.inventory = []
    self.lock = threading.Lock()
```

It creates an empty list (self.inventory) to store the items and a Lock object (self.lock) to ensure thread safety.
```self.lock = threading.Lock():`` A Lock ensures that only one thread can modify the inventory at any given time, preventing data corruption in a multithreaded environment.

4) Adds an item to the inventory in a thread-safe manner.
```python
def add_item(self, item):
    with self.lock:
        self.inventory.append(item)
        print(f"Added to inventory: {item}")
```

```self.inventory.append(item):``` Appends the given item to the inventory list.
```print(f"Added to inventory: {item}"):``` Prints a message indicating that the item was successfully added.

5) This method generates items by creating an initial item using the ItemFactory and then cloning that item to create the specified number of copies.
```python
def generate_items(self, item_type, attributes, count, factory):
    base_item = factory.create_item(item_type, **attributes)
    self.add_item(base_item)
    for _ in range(count - 1):
        cloned_item = base_item.clone()
        self.add_item(cloned_item)
```

```base_item = factory.create_item(item_type, **attributes):``` Creates a new item of the given type (e.g., "Desk", "Desktop") with the provided attributes (e.g., height, material).

```self.add_item(base_item):``` Adds the base item to the inventory.

```for _ in range(count - 1):``` Iterates count - 1 times to create clones of the base item.

```cloned_item = base_item.clone():``` Clones the base item to create a new item.

```self.add_item(cloned_item):``` Adds each cloned item to the inventory.

6) Displays all items currently in the inventory in a thread-safe manner.
```python
def show_inventory(self):
    with self.lock:
        print("\nCurrent Inventory:")
        for item in self.inventory:
            print(item)
        print("-" * 30)
```

```with self.lock:``` Ensures that only one thread can read and print the inventory at a time.

```print(item):``` Prints each item in the inventory.

```print("-" * 30):``` Prints a separator line after displaying the inventory.


## File: main.py

1) Imports
```python
import threading
from inventory_manager import InventoryManager
from inventory_item import ItemFactory
``` 

```import threading:``` This module enables multithreading, allowing multiple parts of the code to run concurrently.

```from inventory_manager import InventoryManager:``` Imports the InventoryManager class from inventory_manager.py.

```from inventory_item import ItemFactory:``` Imports the ItemFactory class from inventory_item.py to create new inventory items.

2) Start
if __name__ == "__main__":
    inventory_manager = InventoryManager()
    factory = ItemFactory()

```if __name__ == "__main__":``` Ensures that the code inside this block runs only when the script is executed directly, not when imported as a module.

```inventory_manager = InventoryManager():``` Creates an instance of InventoryManager.

```factory = ItemFactory():``` Creates an instance of ItemFactory to generate new items.

3) Creates a new thread to run the generate_items method of InventoryManager for creating desks. 
```python
thread1 = threading.Thread(target=inventory_manager.generate_items, args=(
    'Desk', {'height': 75, 'material': 'wood', 'type': 'pupil'}, 3, factory))
```

```thread1 = threading.Thread(...):``` It generates 3 desks with the specified attributes (e.g., height, material, type).

```target=inventory_manager.generate_items:``` Specifies the method to run in the thread.

```args=(...):``` Provides the arguments for the generate_items method, including the item type, attributes, the number of items, and the factory.

4) Creates another thread to generate 3 desktops with the specified attributes (e.g., processor, RAM, type).
```python
thread2 = threading.Thread(target=inventory_manager.generate_items, args=(
    'Desktop', {'processor': 'Intel i5', 'RAM': 16, 'type': 'workstation'}, 3, factory))
```
    
5) Starts both threads, allowing them to run concurrently.
```python
thread1.start()
thread2.start()
```

6) Waits for both threads to complete before continuing with the rest of the program.
```python
thread1.join()
thread2.join()
```

7) Creates a base desk using the factory.
```python
base_desk = factory.create_item('Desk', **{'height': 75, 'material': 'wood', 'type': 'pupil'})
```

8) Clones the base desk and changes its type attribute to teacher.
```python
desk_for_teacher = base_desk.clone(type='teacher')
```

9) Adds the cloned desk to the inventory.
```python
inventory_manager.add_item(desk_for_teacher)
```    
    
10) Displays the final inventory, including all desks and desktops generated by the threads, and the additional teacher's desk.
```python
inventory_manager.show_inventory()
```

## Result

```bash
$ python main.py
Added to inventory: ID: 1, Desk (height: 75, material: wood, type: pupil)
Added to inventory: ID: 2, Desk (height: 75, material: wood, type: pupil)
Added to inventory: ID: 3, Desktop (processor: Intel i5, RAM: 16, type: workstation)
Added to inventory: ID: 4, Desk (height: 75, material: wood, type: pupil)
Added to inventory: ID: 5, Desktop (processor: Intel i5, RAM: 16, type: workstation)
Added to inventory: ID: 6, Desktop (processor: Intel i5, RAM: 16, type: workstation)
Added to inventory: ID: 8, Desk (height: 75, material: wood, type: teacher)

Current Inventory:
ID: 1, Desk (height: 75, material: wood, type: pupil)
ID: 2, Desk (height: 75, material: wood, type: pupil)
ID: 3, Desktop (processor: Intel i5, RAM: 16, type: workstation)
ID: 4, Desk (height: 75, material: wood, type: pupil)
ID: 5, Desktop (processor: Intel i5, RAM: 16, type: workstation)
ID: 6, Desktop (processor: Intel i5, RAM: 16, type: workstation)
ID: 8, Desk (height: 75, material: wood, type: teacher)
------------------------------
```