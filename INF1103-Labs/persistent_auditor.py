
file_name = "inventory.txt"
starting_order_id = 1001
product_name = input("Enter Product Name: ")  
product_quantity = input("Enter Quantity: ")
orders = [[1001, "Wireless Mouse", 2], [1002, "Keyboard", 1], [1003, "USB Cable", 3]]  #this is the initial order
#-----Prev wk3------------
total_inventory, transaction_history = load_inventory()
failed_entries = 0
total_tax = 0  
transaction_history = [product_name, product_quantity, calculate_tax() ]
#-----Functions------

def load_inventory():  #function to read from the file
    try:
        with open(file_name, "r") as file:
            new_inventory = file.readlines()
            total_inventory = int(new_inventory[0].strip())  #first index is inventory
        transaction_history = []
        for line in new_inventory[1:]:
            transaction_history.append(int(line.strip()))  #second index is hist
        return total_inventory, transaction_history    
    except FileNotFoundError:
        return 0,[]  # Return an empty list if the file doesn't exist   

def save_inventory(total_inventory, transaction_history):  #function to write orders to the file
    with open(file_name, "w") as file:
        lines_to_write = [str(total_inventory + "\n")]
        for amount in transaction_history:
            lines_to_write.append(str(amount) + "\n")
            file.writelines(lines_to_write)

def max_order_id():  #function to identify the highest order id
    max_id = starting_order_id
    for order in load_inventory:
        split_order = int(order.split(",")[0]) #splits the orders into integers only(id)    
        if split_order > max_id:
            max_id = split_order
            return max_id  

def generate_order_id(): #func to create new ID
    new_id = max_order_id(load_inventory, starting_order_id) + 1 
    return new_id         

def append_orders(): #func to add new orders to the list n file
    with open(file_name,"a") as file:
        new_order = file.write(str(generate_order_id()), product_name, product_quantity)
        return new_order

  #-------Prev----------

def get_valid_input(): #main input function to get valid input from the user
    user_input = input("Enter a valid integer or 'QUIT' to exit: ")
    if user_input == 'QUIT':
        return "QUIT"
    if user_input.isdigit():
        return int(user_input)
    else:
        print("Invalid input. Please enter a whole number.")
        return None

def process_delivery(total_inventory, stock_int): #processes the delivery, returns new total inventory
    new_value = total_inventory + stock_int
    return new_value 

def calculate_tax(stock_int): #calculates the tax for a specific delivery, returns the tax amount
    tax = stock_int * 0.1
    return tax

def generate_report(total_inventory, failed_entries, total_tax): #final report 
    print("Total Deliveries Processed:", total_inventory)
    print("Total Failed Entries:", failed_entries)
    print("Total Tax Cost:", total_tax)



       
        





#main loop to handle user input and process deliveries

while total_inventory <= 500:

    stock = get_valid_input()

    if stock == 'QUIT':
        save_inventory(total_inventory, transaction_history)
        break
        
        

    elif stock is None:
        failed_entries += 1
        


    else: 
        total_inventory = process_delivery(total_inventory, stock)
        tax_amount = calculate_tax(stock)
        total_tax += tax_amount
        transaction_history.append(stock)  #save txn hist as its confirmed
        print("Total Inventory:", total_inventory)
        print("Tax for this delivery:", tax_amount)
        print("Total failed entries:", failed_entries)



    if total_inventory > 500:
        print("Inventory limit reached. Cannot add more stock.")
        break
        
print("Final Report:")
generate_report(total_inventory, failed_entries, total_tax)




