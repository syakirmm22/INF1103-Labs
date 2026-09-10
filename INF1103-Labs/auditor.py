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
    
        
print("Total Unit Processed:", total_inventory, "Total Failed Entries:", failed_entries)  




          



