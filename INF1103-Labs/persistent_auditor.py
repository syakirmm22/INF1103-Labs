file_name = "inventory.txt"
orders = [10001, "Wireless Mouse", 2], [10002, "Keyboard", 1], [10003, "USB Cable", 3]  #this is the initial order
     


def read_orders():
    try:
        with open(file_name, "r") as file:
            orders = file.readlines()
            return orders
    except FileNotFoundError:
        return [] #Return an empty list if the file doesnt exist

def write_orders():
    with open(file_name, "w") as file:
        file.writelines(orders)
        return orders      
        





def get_load_inventory():





def get_save_inventory():




