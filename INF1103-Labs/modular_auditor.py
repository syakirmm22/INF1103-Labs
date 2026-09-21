#get_valid_input(): Handles the prompt, handles input validation, 
# and returns a valid integer or a "quit" signal.

#process_delivery(current_total, new_value): Calculates the new total and returns it.

#calculate_tax(amount): A new requirement! This function takes a delivery 
# amount and returns the tax (10% of that specific delivery).

#generate_report(total_units, failed_attempts): A dedicated function to print the final summary.

#def functions to be implemented in the modular_auditor.py file

def get_valid_input(): #main input function to get valid input from the user
    user_input = input("Enter a valid integer or 'QUIT' to exit: ")
    if user_input == 'QUIT':
        return "QUIT"
    if user_input.isdigit():
        return int(user_input)
    else:
        print("Invalid input. Please enter a whole number.")
        print("Total failed entries: ", failed_entries+1)
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
total_inventory = 0
failed_entries = 0
total_tax = 0

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
        print("Total Inventory:", total_inventory)
        print("Tax for this delivery:", tax_amount)
        print("Total failed entries:", failed_entries)



    if total_inventory > 500:
        print("Inventory limit reached. Cannot add more stock.")
        break
        
print("Final Report:")
generate_report(total_inventory, failed_entries, total_tax)