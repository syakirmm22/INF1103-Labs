file_name = "inventory.txt"
starting_order_id = 1001
orders = [[1001, "Wireless Mouse", 2], [1002, "Keyboard", 1], [1003, "USB Cable", 3]]  #this is the initial order
     
#-----Functions------

def read_file():  #function to read from the file
    try:
        with open(file_name, "r") as file:
            orders = file.readlines()
            return orders
    except FileNotFoundError:
        return []  # Return an empty list if the file doesn't exist   

def write_orders(orders):  #function to write orders to the file
    with open(file_name, "w") as file:
        file.writelines(orders) 
        return orders  

def max_order_id():  #function to identify the highest order id
    max_id = starting_order_id
    for order in read_file:
        split_order = int(order.split(",")[0]) #splits the orders into integers only(id)    
        if split_order > max_id:
            max_id = split_order
            return max_id  

def generate_order_id(): #func to create new ID
    new_id = max_order_id(read_file, starting_order_id) + 1 
    return new_id         

  

        

product_name = input("Enter Product Name: ")  

product_quantity = input("Enter Quantity: ")
       
        









