import json


#------JSON FILE HANDLING FUNCTIONS------#

def load_inventory(): #function to load inventory data from a JSON file
    try:
        with open("inventories.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [] #returns the default inventory list if the file is not found

def save_inventory(inventories): #function to save inventory data to a JSON file
    with open("inventories.json", "w") as file:
        json.dump(inventories, file)
        print("Saving Inventory...")
        print("All is up to date")


#----MAIN FUNCTIONS----#

def display_inventory(inventories): #function to dislay inventory
    
    for inventory in inventories:
        print(f"Product ID: {inventory['id']}, Name: {inventory['name']}, Price: ${inventory['price']:.2f}, Stock: {inventory['stock']}\n")



def add_inventory(inventories): #function to add new inventory
    
    try:

        new_product = {"id" : input("Enter product ID: \n").strip().upper(),"name" : input("Enter product name: \n"),"price" : float(input("Enter product price: \n")),"stock" : int(input("Enter product stock: \n"))}
    except ValueError:
        print("Invalid entries, please try again.") #PRevent errors to input
        add_inventory(inventories)
        return

    for inventory in inventories:
        if new_product["id"] == inventory["id"]:
            print("Duplicate ID, please enter a unique ID")
            return add_inventory(inventories)


    inventories.append(new_product) #adds the new product to the inventory list
    
    print(f"Product: {new_product['name'] } added successfully.")


def update_stock(inventories):  #function to update stock of an existing product
   
    
    product_id = input(("Enter product ID to update stock (enter 'CANCEL' to cancel): ")).strip().upper()

    if product_id.upper() == "CANCEL":
        print("Stock update canceled.")
        return

    for inventory in inventories:
        if inventory["id"] == product_id:
            try:
                new_stock = int(input("Enter new stock quantity: "))
            except ValueError:
                print("Invalid stock quantity. Please enter a valid integer.")
                update_stock(inventories)
                return
            inventory["stock"] = new_stock #updates the stock of the product
           
            print(f"Stock for product ID: {product_id} updated to {new_stock}")
            break

    
    else:
        print("Product ID not found.")
        update_stock(inventories)  #calls the update_stock function to update stock of a product



def search_inventory(inventories): #function to search for a product
    
    
    product_id = (input("Enter product ID to search (enter 'CANCEL' to cancel): ")).strip().upper()
    
        
    if product_id.upper() == "CANCEL":
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
        search_inventory(inventories)  #calls the search_inventory function to search for a product


#---MAIN MENU FUNCTION---#

print(
    "--------------------------------------------\n"
    "        INVENTORY MANAGEMENT SYSTEM\n"
    "--------------------------------------------\n"
)

inventories = load_inventory() #load inventory first

print("Main Menu:\n")
print("1. Display Inventory\n")
print("2. Add Product\n")
print("3. Update Stock\n")
print("4. Search Product\n")
print("5. Save Inventory\n")
print("6. Exit\n")

while True:
    try: 
        choice = int(input("Enter your choice (1-6): \n"))
    except ValueError:
        print("Option not valid. Please enter a number between 1 and 6.\n")
        continue
    if choice == 1:
        display_inventory(inventories)
    elif choice == 2:
        add_inventory(inventories)
    elif choice == 3:
        update_stock(inventories)
    elif choice == 4:
        search_inventory(inventories)
    elif choice == 5:
        save_inventory(inventories)
    elif choice == 6:
        print("Exiting the program.\n")
        
        print("Saving inventory before exit....")

        save_inventory(inventories) #final save

        print("All done. Goodbye")
        break    #exit the loop and terminate the program        