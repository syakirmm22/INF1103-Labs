file_name = "inventory.txt"
#orders = [[1001, "Wireless Mouse", 2], [1002, "Keyboard", 1], [1003, "USB Cable", 3]]  #this is the initial order
     


def load_inventory():
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()
            if not lines:
                return 0, []
            total = float(lines[0].strip())
            history = [float(line.strip()) for line in lines[1:]]
            return total, history
    except FileNotFoundError:
        return 0, [] #Return an empty list if the file doesnt exist

def save_inventory(total, history):  
    with open(file_name, "w") as file:
        file.write(str(total) + "\n")
        for amount in history:
            file.write(str(amount) + "\n")

        

        
       
        









