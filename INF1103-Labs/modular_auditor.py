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
        return None

def process_delivery(total_inventory, stock_int): #processes the delivery, returns new total inventory
    new_value = total_inventory + stock_int
    return new_value 

def calculate_tax(stock_int): #calculates the tax for a specific delivery, returns the tax amount
    tax = stock_int * 0.1
    return tax









total_inventory = 0
failed_entries = 0

while total_inventory <= 500:

    stock = input("Enter the stock inventory or enter 'QUIT' to exit: ")

    if stock == 'QUIT':
        break

    if stock.isdigit():
        stock_int = int(stock)
        total_inventory += stock_int
        print("Total inventory:", total_inventory)

    else: 
        print("Negative value/Invalid entry. Please enter a whole number and not in word form.")
        failed_entries += 1   


    if total_inventory > 500:
        print("Inventory limit reached. Cannot add more stock.")
        break
        
print("Total Deliveries Processed:", total_inventory, "Total Failed Entries:", failed_entries)  