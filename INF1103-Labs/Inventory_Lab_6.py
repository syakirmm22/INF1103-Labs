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

#load n save inventory

def load_inventory(inventory):
    try:
        with open("inventory.json", "r") as file:

            data = json.load(file)  #lists of dict

            for item in data:
                product = Product(item["id"], item["name"], item["price"], item["stock"])
                inventory.add_product(product)
    
    except FileNotFoundError:
        print("No Saved Inventory Found. Starting Empty")

    

def save_inventory(inventory):
    print("Saving Inventory....")
    data = []
    for product in inventory.get_all_products():
        data.append({
            "id": product.get_product_id(),
            "name": product.get_name(),
            "price": product.get_price(),
            "stock": product.get_stock()
        })

    with open("inventory.json", "w") as file:
        json.dump(data, file, indent=4)
        
        print("Save Completed!")
            
        




#start of class product


class Product:
    def __init__(self, product_id, name, price, stock):
        self.__name = name
        self.__product_id = product_id
        self.__price = price
        self.__stock = stock

    #getters(read only for other classes)

    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    #methods

    def update_stock(self, quantity):
        if quantity + self.__stock < 0:
            return False
        else:
            self.__stock += quantity
            return True

    def display_information(self):
            print(f"ID: {self.__product_id}")
            print(f"Name: {self.__name}")
            print(f"Price: ${self.__price:.2f}")
            print(f"Stock: {self.__stock}") 

#class of inventory

class Inventory:
    def __init__(self):
        self.__products = []

    # methods

    def add_product(self, product):
        self.__products.append(product)

    def search_product(self, product_id):
        for product in self.__products:
            if product_id == product.get_product_id():
                return product
        
        return None

                

    def display_all(self):
        if len(self.__products) == 0:
            print("No products yet")
        else:
            for product in self.__products:
                product.display_information()
                print() #to separate the prints


    def get_all_products(self):
        return self.__products            



#---MAIN MENU FUNCTION---#

print(
    "--------------------------------------------\n"
    "        INVENTORY MANAGEMENT SYSTEM\n"
    "--------------------------------------------\n"
)




#Creating the Products

inventory = Inventory() #creating the inventory object from its class

load_inventory(inventory) #load inventory first

if len(inventory.get_all_products()) == 0:   
    inventory.add_product(Product("P001", "Mouse", 50.00, 125))
    inventory.add_product(Product("P002", "Keyboard", 80.00, 105))


                
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

        new_product = Product(product_id, name, price, stock)
        inventory.add_product(new_product)
        print(f"{name} successfully added\n")


    elif choice == 3:
        
        product_id = input("Enter Product ID: \n").strip().upper()
          
        product = inventory.search_product(product_id)

        if product is None:
            print("No Product Found")
            continue

        else:
            try:                
                quantity = int(input("Enter Quantity To Add/Remove: \n"))
            except ValueError:
                print("Please enter an integer")    
                continue

            if product.update_stock(quantity):

                print(f"Stock has been updated to {product.get_stock()}")
            else:
                print("Not Enough Stock To Remove")    

       

    elif choice == 4:

        product_id = input("Enter Product ID: \n").strip().upper()

        product = inventory.search_product(product_id)
        
        if product is None:
            print("No Product Found")
            continue

        else:
            product.display_information()


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
        
        






        






            
            



    




