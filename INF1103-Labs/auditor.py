total_inventory = 0
failed_entries = 0

stock = (input("Enter the stock inventory: "))

if stock.isdigit():
    stock_int = int(stock)
    total_inventory += stock_int
    print("Total inventory:", total_inventory)



