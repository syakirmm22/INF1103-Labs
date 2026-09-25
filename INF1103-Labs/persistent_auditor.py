
     


def read_orders():
    try:
        with open(file_name, "r") as file:
            orders = file.readlines()
            return orders
    except FileNotFoundError:
        return [] #Return an empty list if the file doesnt exist

def write_orders():
    try:        





def get_load_inventory():





def get_save_inventory():




