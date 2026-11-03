import product
class PhysicalProduct(product.Product):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    #getter(read only for other classes)

    @property
    def weight(self):
        return self.__weight

    #setters (for internal use only)

    @weight.setter
    def set_weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = value

    #methods

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")