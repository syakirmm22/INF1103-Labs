
from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, product_id, name, price, stock):
        self.__name = name
        self.__product_id = product_id
        self.__price = price
        self.__stock = stock

    #getters(read only for other classes)

    @abstractmethod

    def get_fulfillment_info(self):
        pass

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