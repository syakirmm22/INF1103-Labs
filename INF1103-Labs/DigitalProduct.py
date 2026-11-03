import product
class DigitalProduct(product.Product):
    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)
        self._download_size = download_size

    #getter(read only for other classes)

    def get_download_size(self):
        return self._download_size

    #methods

    def display_information(self):
        super().display_information()
        print(f"Download Size: {self._download_size} MB")