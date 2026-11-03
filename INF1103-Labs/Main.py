#class name:
#  product 

#attributes: 

# - __name: string
# - __product_id: string
# - __price: float
# - __stock: int

# + __init__(product_id, name, price, stock)

#methods:

# + update_stock(quantity : int):void (can remove or add stock)
# + display_information():void



#class name:
#  inventory

#attributes: 

# - __products: list[Product]

#methods: 

# + add_product(produt : Product): void
# + search_product(product_id : String): Product
# + display_all(): void
# + get_all_products(): list[Product]




import json
import inventory 
import product
import DigitalProduct
import PhysicalProduct

#load n save inventory

def load_inventory(inventory):
    try:
        with open("inventory.json", "r") as file:

            data = json.load(file)  #lists of dict

            for item in data:
                loaded_product = product.Product(item["id"], item["name"], item["price"], item["stock"])
                inventory.add_product(loaded_product)

    except FileNotFoundError:
        print("No Saved Inventory Found. Starting Empty")


def save_inventory(inventory):
    data = []   #lists of dict

    for p in inventory.get_all_products():
        data.append({
            "id": p.get_product_id(),
            "name": p.get_name(),
            "price": p.get_price(),
            "stock": p.get_stock()
        })

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)

    print("Inventory Saved Successfully\n")





#---MAIN MENU FUNCTION---#

print(
    "--------------------------------------------\n"
    "        INVENTORY MANAGEMENT SYSTEM\n"
    "--------------------------------------------\n"
)




#Creating the Products

inventory = inventory.Inventory() #creating the inventory object from its class

load_inventory(inventory) #load inventory first

if len(inventory.get_all_products()) == 0:   
    inventory.add_product(product.Product("P001", "Mouse", 50.00, 125))
    inventory.add_product(product.Product("P002", "Keyboard", 80.00, 105))


                
while True:

    print("Main Menu:")
    print("1. Display All Products")
    print("2. Add a Product")
    print("3. Update Stock")
    print("4. Search For a Product")
    print("5. Save Inventory")
    print("6. Exit")   
    try:
        choice = int(input("Enter your choice (1-6): \n"))

    except ValueError:
        print("Invalid Option. Try Again\n")    
        continue

    if choice == 1:
        inventory.display_all()

    elif choice == 2:
        try:

            product_id = input("Enter Product ID: \n").strip().upper()

            if inventory.search_product(product_id) is not None:
                print("Duplicate ID, Try Again")
                continue


            name = input("Enter Product Name: \n") 
            price = float(input("Enter Product Price: \n"))   
            stock = int(input("Enter Product Stock: \n"))
        except ValueError:
            print('Invalid Input. Try Again')    
            continue

        print("Select Product Type:")
        print("1. Physical Product")
        print("2. Digital Product")
        try:
            product_type = int(input("Enter your choice (1-2): \n"))
        except ValueError:
            print("Invalid Option. Try Again\n")    
            continue

        if product_type == 1:
            try:
                weight = float(input("Enter Product weight (in kg): \n"))
            except ValueError:
                print("Invalid Input. Try Again\n")    
                continue

            new_product = PhysicalProduct.PhysicalProduct(product_id, name, price, stock, weight)
            inventory.add_product(new_product)
            print(f"{name} successfully added\n")
                

        elif product_type == 2:
            try:
                file_size = float(input("Enter Product file size (in MB): \n"))
            except ValueError:
                print("Invalid Input. Try Again\n")    
                continue

            new_product = DigitalProduct.DigitalProduct(product_id, name, price, stock, file_size)
            inventory.add_product(new_product)
            print(f"{name} successfully added\n")

        else:
            print("Invalid Option. Try Again\n")    
            continue    



    elif choice == 3:
        
        product_id = input("Enter Product ID: \n").strip().upper()
          
        found_product = inventory.search_product(product_id)

        if found_product is None:
            print("No Product Found")
            continue

        else:
            try:                
                quantity = int(input("Enter Quantity To Add/Remove: \n"))
            except ValueError:
                print("Please enter an integer")    
                continue

            if found_product.update_stock(quantity):

                print(f"Stock has been updated to {found_product.get_stock()}")
            else:
                print("Not Enough Stock To Remove")    

       

    elif choice == 4:

        product_id = input("Enter Product ID: \n").strip().upper()

        found_product = inventory.search_product(product_id)
        
        if found_product is None:
            print("No Product Found")
            continue

        else:
            found_product.display_information()


    elif choice == 5:
        save_inventory(inventory)


    elif choice == 6:
            print("Exiting the program.\n")
            
            print("Saving inventory before exit....")
    
            save_inventory(inventory)
            
            print("All done. Goodbye")
            break    #exit the loop and terminate the program           
            
    else:
        print("Please Enter (1-6) Only")
        
        






        






            
            



    




