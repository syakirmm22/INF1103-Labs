import product
import CanBeShipped

class PhysicalProduct(product.Product, CanBeShipped.CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight

    #getter(read only for other classes)

    @property
    def weight(self):
        return self.__weight

  

    #setters (for internal use only)

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError("Weight cannot be negative.")
        self.__weight = value



    #methods

    def get_fulfillment_info(self):
        print(f"{self.get_name()} requires physical shipping.")

    def display_information(self):
        super().display_information()
        print(f"Weight: {self.__weight} kg")
        print(f"Shipping Cost: ${self.calculate_shipping_cost():.2f}")

    def calculate_shipping_cost(self):
        #COST BASED ON WEIGHT ( $5 PER KG)
        return self.__weight * 5.00
