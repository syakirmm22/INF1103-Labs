
starting_order_id = 1001
product_name = input("Enter Product Name: ")  
product_quantity = input("Enter Quantity: ")
orders = [[1001, "Wireless Mouse", 2], [1002, "Keyboard", 1], [1003, "USB Cable", 3]]  #this is the initial order
#-----Prev wk3------------


#-----Functions------

file_name = "inventory.txt"

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
        lines_to_write = [(str(total_inventory) + "\n")]
        for amount in transaction_history:
            lines_to_write.append(str(amount) + "\n")
        
        file.writelines(lines_to_write)

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



       
        

total_inventory, transaction_history = load_inventory()
failed_entries = 0
total_tax = 0  



#main loop to handle user input and process deliveries

while total_inventory <= 500:

    stock = get_valid_input()

    if stock == 'QUIT':
        
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

save_inventory(total_inventory, transaction_history)     #saves even when the limit is hit   
print("Final Report:")
generate_report(total_inventory, failed_entries, total_tax)




