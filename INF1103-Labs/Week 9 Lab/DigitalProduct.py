import product
class DigitalProduct(product.Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self.download_size = download_size

    #getter(read only for other classes)

    @property
    def download_size(self):
        return self._download_size


    #setters (for internal use only)

    @download_size.setter
    def download_size(self, value):
        if value < 0:
            raise ValueError("Download size cannot be negative.")
        self._download_size = value


    #methods

    def get_fulfillment_info(self):
            print(f"{self.get_name()} will be delivered digitally.")

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")