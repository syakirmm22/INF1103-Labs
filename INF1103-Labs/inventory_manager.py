import json

inventories = [       #inventory list n dictionary
    {"id" : 1001, "name" : "Laptop", "price" : 1200.00, "stock" : 45},

{"id" : 1002, "name" : "Mouse", "price" : 50.00, "stock" : 150},

{"id" : 1003, "name" : "Keyboard", "price" : 70.00, "stock" : 134}
]

#------JSON FILE HANDLING FUNCTIONS------#

def load_inventory(): #function to load inventory data from a JSON file
    try:
        with open("inventories.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return inventories  #returns the default inventory list if the file is not found

def save_inventory(inventories): #function to save inventory data to a JSON file
    with open("inventories.json", "w") as file:
        json.dump(inventories, file)


#----MAIN FUNCTIONS----#

def display_inventory(): #function to dislay inventory
    inventories = load_inventory()
    inventories.json.writelines(inventories)
    
    #for inventory in inventories:
      #print(inventory["id"], inventory["name"], inventory["price"], inventory["stock"])


def add_inventory(): #function to add new inventory
    inventories = load_inventory()

    new_product = {"id" : int(input("Enter product ID: ")),"name" : input("Enter product name: "),"price" : float(input("Enter product price: ")),"stock" : int(input("Enter product stock: "))}

    inventories.append(new_product) #adds the new product to the inventory list
    save_inventory(inventories)  #saves the updated inventory list to the JSON file
