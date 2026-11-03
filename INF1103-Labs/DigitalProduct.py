import product
class DigitalProduct(product.Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    #getter(read only for other classes)

    @property
    def download_size(self):
        return self._download_size


    #setters (for internal use only)

    @download_size.setter
    def set_download_size(self, value):
        if value < 0:
            raise ValueError("Download size cannot be negative.")
        self._download_size = value


    #methods

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")