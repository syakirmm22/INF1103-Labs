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
