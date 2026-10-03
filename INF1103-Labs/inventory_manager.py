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
    for inventory in inventories:
        print(f"Product ID: {inventory['id']}, Name: {inventory['name']}, Price: ${inventory['price']:.2f}, Stock: {inventory['stock']}\n")



def add_inventory(): #function to add new inventory
    inventories = load_inventory()

    new_product = {"id" : int(input("Enter product ID: \n")),"name" : input("Enter product name: \n"),"price" : float(input("Enter product price: \n")),"stock" : int(input("Enter product stock: \n"))}

    inventories.append(new_product) #adds the new product to the inventory list
    save_inventory(inventories)  #saves the updated inventory list to the JSON file
    print(f"Product: {new_product['name'] } added successfully.")


def update_stock():  #function to update stock of an existing product
    inventories = load_inventory()
    try:
        product_id = int(input("Enter product ID to update stock (enter '0' to cancel): "))
        
    except ValueError:
        print("Invalid product ID. Please enter a valid integer.")
        update_stock()
        return

    if product_id == 0:
        print("Stock update canceled.")
        return

    for inventory in inventories:
        if inventory["id"] == product_id:
            try:
                new_stock = int(input("Enter new stock quantity: "))
            except ValueError:
                print("Invalid stock quantity. Please enter a valid integer.")
                update_stock()
                return
            inventory["stock"] = new_stock #updates the stock of the product
            save_inventory(inventories)  #saves the updated inventory list to the JSON file
            print(f"Stock for product ID: {product_id} updated to {new_stock}")
            break

    
    else:
        print("Product ID not found.")
        update_stock()  #calls the update_stock function to update stock of a product



def search_inventory(): #function to search for a product
    inventories = load_inventory()
    try:
        product_id = int(input("Enter product ID to search (enter '0' to cancel): "))
    except ValueError:
        print("Invalid product ID. Please enter a valid integer.")
        search_inventory()
        return
    if product_id == 0:
        print("Search canceled.")
        return

    for inventory in inventories:
        if product_id == inventory["id"]:
            print(f"Product found: Product ID: {inventory['id']}\n")
            print(f"Name: {inventory['name']}\n")
            print(f"Price: ${inventory['price']:.2f}\n")
            print(f"Stock: {inventory['stock']}\n")
            break
    else:
        print("Product not found.")
        search_inventory()  #calls the search_inventory function to search for a product


#---MAIN MENU FUNCTION---#

print(
    "--------------------------------------------\n"
    "        INVENTORY MANAGEMENT SYSTEM\n"
    "--------------------------------------------\n"
)

print("Main Menu:\n")
print("1. Display Inventory\n")
print("2. Add Product\n")
print("3. Update Stock\n")
print("4. Search Product\n")
print("5. Exit\n")

while True:
    try: 
        choice = int(input("Enter your choice (1-5): \n"))
    except ValueError:
        print("Option not valid. Please enter a number between 1 and 5.\n")
        continue
    if choice == 1:
        display_inventory()
    elif choice == 2:
        add_inventory()
    elif choice == 3:
        update_stock()
    elif choice == 4:
        search_inventory()
    elif choice == 5:
        print("Exiting the program.\n")
        break    #exit the loop and terminate the program        