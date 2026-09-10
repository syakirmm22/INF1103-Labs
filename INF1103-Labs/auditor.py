total_inventory = 0
failed_entries = 0

stock = (input("Enter the stock inventory: "))

while total_inventory < 500:

    stock = input("Enter the stock inventory or enter 'QUIT' to exit: ")

    if stock == 'QUIT':
        break

    if stock.isdigit():
        stock_int = int(stock)
        total_inventory += stock_int
        print("Total inventory:", total_inventory)

    elif int(stock) < 0:
        print("Invalid entry. Stock cannot be negative.")
        failed_entries += 1
    else: 
        print("Invalid entry. Please enter a whole number and not in word form.")
        failed_entries += 1        



