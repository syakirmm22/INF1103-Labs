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
                
         




            
            



    




