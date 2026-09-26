


#-----Functions------

file_name = "inventory.txt"
next_order_id = 1001







def load_inventory():  #function to read from the file
    try:
        with open(file_name, "r") as file:
            new_inventory = file.readlines()

            if not new_inventory:
                return 0, []
            
            total_inventory = int(new_inventory[0].strip())  #first index is id
        
        transaction_history = []
        for line in new_inventory[1:]:
            parts = line.strip()

            if not line:
                continue

            parts = line.split(",")

            if len(parts) >= 3:
                order_id = int(parts[0])
                name = parts[1]
                quantity = int(parts[2])
            
        transaction_history.append([order_id, name, quantity])
        return total_inventory, transaction_history    
    except FileNotFoundError:
        return 0,[]  # Return an empty list if the file doesn't exist   

def save_inventory(total_inventory, transaction_history):  #function to write orders to the file
    with open(file_name, "w") as file:
        lines_to_write = [(str(total_inventory) + "\n")]
        for order in transaction_history:
            order_id = order[0]
            name = order[1]
            quantity = order[2]

            line = str(order_id) + "," + name + "," + str(quantity) + "\n"
            lines_to_write.append(line)
        
        file.writelines(lines_to_write)

  #-------Prev----------

def get_valid_input(): #main input function to get valid input from the user
    product_name = input("Enter Product Name (or QUIT to exit): ")
    if product_name == 'QUIT':
        return 'QUIT', 'QUIT'

    quantity_input = input("Enter Quantity: ")
    if quantity_input.isdigit():
        return product_name, int(quantity_input)
    else:
        print("Invalid input. Please enter a whole number.")
        return None, None



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

def max_order_id(transaction_history, next_order_id):  #function to get the maximum order ID
    max_id = next_order_id - 1
    for order in transaction_history:
        split_order = order[0]  
        if split_order > max_id:
            max_id = split_order
    return max_id

def generate_new_id(transaction_history, next_order_id):
    new_id = max_order_id(transaction_history, next_order_id) + 1
    return new_id

       
        

total_inventory, transaction_history = load_inventory()
next_order_id = generate_new_id(transaction_history, 1000)
failed_entries = 0
total_tax = 0  




#main loop to handle user input and process deliveries

while total_inventory <= 500:

    product_name, product_quantity = get_valid_input()

    

    if product_name == 'QUIT':
        
        break
        
        

    elif product_name is None:
        failed_entries += 1
        


    else: 
        total_inventory = process_delivery(total_inventory, product_quantity)
        tax_amount = calculate_tax(product_quantity)
        total_tax += tax_amount
        new_order = [next_order_id, product_name, product_quantity]
        transaction_history.append(new_order)  #save txn hist as its confirmed
        next_order_id = generate_new_id(transaction_history, next_order_id)
        
       
        print("New Order Added: ", new_order)
        print("Total Inventory:", total_inventory)
        print("Tax for this delivery:", tax_amount)
        print("Total failed entries:", failed_entries)



    if total_inventory > 500:
        print("Inventory limit reached. Cannot add more stock.")
        break

save_inventory(total_inventory, transaction_history)     #saves even when the limit is hit   
print("Final Report:")
generate_report(total_inventory, failed_entries, total_tax)




