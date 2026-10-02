import json

inventories = [       #inventory list n dictionary
    {"id" : 1001, "name" : "Laptop", "price" : 1200.00, "stock" : 45},

{"id" : 1002, "name" : "Mouse", "price" : 50.00, "stock" : 150},

{"id" : 1003, "name" : "Keyboard", "price" : 70.00, "stock" : 134}
]

def load_inventory(): #function to load inventory data from a JSON file
    with open("inventories.json", "r") as file:
        return json.load(file)

def save_inventory(inventories): #function to save inventory data to a JSON file
    with open("inventories.json", "w") as file:
        json.dump(inventories, file)


#----MAIN FUNCTIONS----#

def display_inventory(): #function to dislay inventory
    inventories = load_inventory()
    for inventory in inventories:
      print(inventory["id"], inventory["name"], inventory["price"], inventory["stock"])





